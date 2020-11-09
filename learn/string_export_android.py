#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import xml.dom.minidom

# v2: reduce code

# language list:
# en -- fr -- sp -- cn -- cz -- dutch -- german -- Hu

file_name = 'vihealth_strings_5_27.xlsx'
strings = pd.read_excel(file_name, sheet_name=0, index_col=0)

# language doc list
key_list = ["en", "fr", "sp", "cn", "hk", "cz", "dutch", "german", "Hu"]


if __name__ == '__main__':

    for i in range(8):
        doc = xml.dom.minidom.Document()
        doc_root = doc.createElement('resources')
        doc.appendChild(doc_root)

        for index, row in strings.iterrows():
            if pd.notnull(row['android_key']) and pd.notnull(row[key_list[i]]):
                node = doc.createElement('string')
                node.setAttribute('name', row['android_key'])
                node.appendChild(doc.createTextNode(str(row[key_list[i]])))

                doc_root.appendChild(node)

        file = './strings/android_strings_%s.xml' % key_list[i]
        with open(file, 'w', encoding='utf-8') as fp:
            doc.writexml(fp, indent='\t', addindent='\t', newl='\n', encoding="utf-8")
            print('%s strings exported' % key_list[i])
