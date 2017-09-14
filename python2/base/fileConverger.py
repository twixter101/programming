import sys


def convergeFile(inputFile):
    print inputFile
    inFile = open(inputFile, 'r+')
    rawData = inFile.readlines()
    line_number = 0
    line_processed = 0
    type_pc_clear = 0
    type_btmuwebach = 0
    fileRecordDictList = []
    entityList = []

    for inputData in rawData:
        line = inputData
        line_number += 1
        line_type = line[191:221]

        if line_type.lower().rstrip() == 'type1':
            line_processed += 1
            type_pc_clear += 1
            entity = line[100:108]
            company_name = line[58:88]
            fileRecordDictList.append('{}\t{}\t{}'.format(entity, company_name, line))
        elif line_type.lower().rstrip() == 'type2':
            line_processed += 1
            type_btmuwebach += 1
            company_name = line[58:88]
            fileRecordDictList.append('{}\t{}\t{}'.format(entity, company_name, line))
        #else:
        #    print line

    fileRecordDictList.sort()

    entity_count = 0
    prev_entity = ''
    outputData = []
    entityDict = {}
    blobList = ''
    for sortedData in fileRecordDictList:
        line = sortedData.split('\t')
        curr_entity = line[0]
        if prev_entity == '':
            blobList = '{}'.format(line[2][:-2])
        else:
            if prev_entity != curr_entity:
                blobList += '|{}'.format(line[2][:-2])
            else:
                entityDict = {'entity': prev_entity, 'blob': blobList}
                outputData.append(entityDict)
                entity_count += 1
                blobList = '{}'.format(line[2][:-2])
        prev_entity = curr_entity

    if prev_entity != '':
        entityDict = {'entity': prev_entity, 'blob': blobList}
        outputData.append(entityDict)
        entity_count += 1

    print 'line_number: {}'.format(line_number)
    print 'line_processed: {}'.format(line_processed)
    print 'type_pc_clear: {}'.format(type_pc_clear)
    print 'type_btmuwebach: {}'.format(type_btmuwebach)
    print 'entity_count: {}'.format(entity_count)

    inFile.close()

    outFile = open('{}.txt'.format(inputFile), 'w+')
    for line in outputData:
        #for id, values in line.items():
        #    outFile.write(':'.join([id] + values.split(':')) + '\n')
        outFile.write('{}\t{}\n'.format(line['entity'], line['blob']))

    outFile.close()


if __name__ == '__main__':
    if len(sys.argv) == 2:
        convergeFile(sys.argv[1])
