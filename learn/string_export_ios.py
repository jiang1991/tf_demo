#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd

# language list:
# en -- fr -- sp -- cn -- cz -- dutch -- german -- Hu

file_name = 'vihealth_strings.xlsx'
strings = pd.read_excel(file_name, sheet_name=0, index_col=0)

strings = strings.sort_values(['ios_index'], ascending=True)

# language doc list
key_list = ["en", "fr", "sp", "cn", "cz", "dutch", "german", "Hu"]

if __name__ == '__main__':

    for i in range(8):

        doc = ""

        for index, row in strings.iterrows():

            if pd.notnull(row['ios_key']):
                doc = doc + ('\"{0}\" = \"{1}\";\n'.format(str(row['ios_key']), str(row[key_list[i]])))
                # doc = doc + ('\"{0}\" = \"{1}\"\n'.format('key', 'value'))

        file = './strings/ios_strings_%s.txt' % key_list[i]
        with open(file, 'w', encoding='utf-8') as file:
            file.write(doc)
            print('%s strings exported' % key_list[i])
