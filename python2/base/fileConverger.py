import sys


TYPE_NAME_1 = ''
TYPE_NAME_2 = ''

LEN_ATTR_01 = 9
LEN_ATTR_02 = 9
LEN_ATTR_03 = 6
LEN_ATTR_04 = 30
LEN_ATTR_05 = 30
LEN_ATTR_06 = 10
LEN_ATTR_07 = 10 
LEN_ATTR_08 = 9
LEN_ATTR_09 = 15
LEN_ATTR_10 = 15
LEN_ATTR_11 = 9
LEN_ATTR_12 = 9
LEN_ATTR_13 = 17
LEN_ATTR_14 = 30
LEN_ATTR_15 = 16 

OFFSET_ATTR_01 = 0
OFFSET_ATTR_02 = OFFSET_ATTR_01 + LEN_ATTR_01 + 1
OFFSET_ATTR_03 = OFFSET_ATTR_02 + LEN_ATTR_02 + 1
OFFSET_ATTR_04 = OFFSET_ATTR_03 + LEN_ATTR_03 + 1
OFFSET_ATTR_05 = OFFSET_ATTR_04 + LEN_ATTR_04 + 1
OFFSET_ATTR_06 = OFFSET_ATTR_05 + LEN_ATTR_05 + 1
OFFSET_ATTR_07 = OFFSET_ATTR_06 + LEN_ATTR_06 + 1
OFFSET_ATTR_08 = OFFSET_ATTR_07 + LEN_ATTR_07 + 1
OFFSET_ATTR_09 = OFFSET_ATTR_08 + LEN_ATTR_08 + 1
OFFSET_ATTR_10 = OFFSET_ATTR_09 + LEN_ATTR_09 + 1
OFFSET_ATTR_11 = OFFSET_ATTR_10 + LEN_ATTR_10 + 1
OFFSET_ATTR_12 = OFFSET_ATTR_11 + LEN_ATTR_11 + 1
OFFSET_ATTR_13 = OFFSET_ATTR_12 + LEN_ATTR_12 + 1
OFFSET_ATTR_14 = OFFSET_ATTR_13 + LEN_ATTR_13 + 1
OFFSET_ATTR_15 = OFFSET_ATTR_14 + LEN_ATTR_14 + 1


def convergeFile(inputFile):
    print inputFile
    inFile = open(inputFile, 'r+')
    rawData = inFile.readlines()
    line_number = 0
    line_processed = 0
    type_1 = 0
    type_2 = 0
    fileRecordDictList = []
    entityList = []

    for inputData in rawData:
        line = inputData
        line_number += 1
        line_type = line[191:221]

        if line_type.lower().rstrip() == TYPE_NAME_1.lower():
            line_processed += 1
            type_1 += 1
            entity_id = line[100:108]
            company_name = line[58:88]
            fileRecordDictList.append('{}|{}|{}'.format(entity_id, company_name, line))
        elif line_type.lower().rstrip() == TYPE_NAME_2.lower():
            line_processed += 1
            type_2 += 1
            entity_id = line[101:110]
            company_name = line[58:88]
            fileRecordDictList.append('{}|{}|{}'.format(entity_id, company_name, line))
        #else:
        #    print line

    fileRecordDictList.sort()

    blob_header = "<GAHtml<tr><th>Company Name</th><th>Company ID</th><th>Account Number></th></tr>"
    blob_trailer = "</GAHtml>"

    entity_count = 0
    prev_entity = ''
    prev_company = ''
    outputData = []
    entityDict = {}
    blobList = ''
    for sortedData in fileRecordDictList:
        line = sortedData.split('|')
        curr_entity = line[0]
        curr_company = line[1].rstrip()
        if prev_entity == '':
            blobList = '{}{}'.format(blob_header, processDetailData(line[2][:-2]))
            prev_company = curr_company
        else:
            if prev_entity != curr_entity:
                blobList += '{}'.format(processDetailData(line[2][:-2]))
                prev_company = curr_company
            else:
                blobList += blob_trailer
                entityDict = {'entity_id': prev_entity, 'company_name': prev_company, 'detail_blob': blobList}
                outputData.append(entityDict)
                entity_count += 1
                blobList = '{}{}'.format(blob_header, processDetailData(line[2][:-2]))
        prev_entity = curr_entity

    if prev_entity != '':
        blobList += blob_trailer
        entityDict = {'entity_id': prev_entity, 'company_name': prev_company, 'detail_blob': blobList}
        outputData.append(entityDict)
        entity_count += 1

    print 'line_number: {}'.format(line_number)
    print 'line_processed: {}'.format(line_processed)
    print 'type_1: {}'.format(type_1)
    print 'type_2: {}'.format(type_2)
    print 'entity_count: {}'.format(entity_count)

    inFile.close()

    outFile = open('{}.txt'.format(inputFile), 'w+')
    for line in outputData:
        #for id, values in line.items():
        #    outFile.write(':'.join([id] + values.split(':')) + '\n')
        outFile.write('{}|{}|{}\n'.format(line['entity_id'], line['company_name'], line['detail_blob']))

    outFile.close()


def processDetailData(detailData):
    processedData = '<tr><td>{}</td><td>{}</td><td>{}</td></tr>'.format(
        detailData[OFFSET_ATTR_05:OFFSET_ATTR_05 + LEN_ATTR_05],
        detailData[OFFSET_ATTR_07:OFFSET_ATTR_07 + LEN_ATTR_07],
        detailData[OFFSET_ATTR_13:OFFSET_ATTR_13 + LEN_ATTR_13]
        )
    return processedData


if __name__ == '__main__':
    if len(sys.argv) == 2:
        convergeFile(sys.argv[1])
