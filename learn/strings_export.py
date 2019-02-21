#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import xml.dom.minidom
import numpy as np
import sys
import io

# 改变标准输出的默认编码
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

file_name = 'vihealth_strings.xlsx'
strings = pd.read_excel(file_name, sheet_name=0, index_col=0)


if __name__ == '__main__':
    # create

    # en
    tsl_en = xml.dom.minidom.Document()
    tsl_en_root = tsl_en.createElement('resources')
    tsl_en.appendChild(tsl_en_root)

    # fr
    tsl_fr = xml.dom.minidom.Document()
    tsl_fr_root = tsl_fr.createElement('resources')
    tsl_fr.appendChild(tsl_fr_root)

    # sp
    tsl_sp = xml.dom.minidom.Document()
    tsl_sp_root = tsl_sp.createElement('resources')
    tsl_sp.appendChild(tsl_sp_root)

    # cn
    tsl_cn = xml.dom.minidom.Document()
    tsl_cn_root = tsl_cn.createElement('resources')
    tsl_cn.appendChild(tsl_cn_root)

    # cz
    tsl_cz = xml.dom.minidom.Document()
    tsl_cz_root = tsl_cz.createElement('resources')
    tsl_cz.appendChild(tsl_cz_root)

    # dutch -- nl
    tsl_nl = xml.dom.minidom.Document()
    tsl_nl_root = tsl_nl.createElement('resources')
    tsl_nl.appendChild(tsl_nl_root)

    # german -- de
    tsl_de = xml.dom.minidom.Document()
    tsl_de_root = tsl_de.createElement('resources')
    tsl_de.appendChild(tsl_de_root)

    # hu
    tsl_hu = xml.dom.minidom.Document()
    tsl_hu_root = tsl_hu.createElement('resources')
    tsl_hu.appendChild(tsl_hu_root)

    for index, row in strings.iterrows():
        if pd.notnull(row['android_index']):
            # en
            nodeStr_en = tsl_en.createElement('string')
            nodeStr_en.setAttribute('name', row['android_key'])
            nodeStr_en.appendChild(tsl_en.createTextNode(row['en']))

            tsl_en_root.appendChild(nodeStr_en)

            # fr
            nodeStr_fr = tsl_fr.createElement('string')
            nodeStr_fr.setAttribute('name', str(row['android_key']))
            nodeStr_fr.appendChild(tsl_fr.createTextNode(str(row['fr'])))

            tsl_fr_root.appendChild(nodeStr_fr)

            # sp
            nodeStr_sp = tsl_sp.createElement('string')
            nodeStr_sp.setAttribute('name', str(row['android_key']))
            nodeStr_sp.appendChild(tsl_sp.createTextNode(str(row['sp'])))

            tsl_sp_root.appendChild(nodeStr_sp)

            # cn
            nodeStr_cn = tsl_cn.createElement('string')
            nodeStr_cn.setAttribute('name', str(row['android_key']))
            nodeStr_cn.appendChild(tsl_cn.createTextNode(str(row['cn'])))

            tsl_cn_root.appendChild(nodeStr_cn)

            # cz
            nodeStr_cz = tsl_cz.createElement('string')
            nodeStr_cz.setAttribute('name', str(row['android_key']))
            nodeStr_cz.appendChild(tsl_cz.createTextNode(str(row['cz'])))

            tsl_cz_root.appendChild(nodeStr_cz)

            # dutch -- nl
            nodeStr_nl = tsl_nl.createElement('string')
            nodeStr_nl.setAttribute('name', str(row['android_key']))
            nodeStr_nl.appendChild(tsl_nl.createTextNode(str(row['dutch'])))

            tsl_nl_root.appendChild(nodeStr_nl)

            # german -- de
            nodeStr_de = tsl_de.createElement('string')
            nodeStr_de.setAttribute('name', str(row['android_key']))
            nodeStr_de.appendChild(tsl_de.createTextNode(str(row['german'])))

            tsl_de_root.appendChild(nodeStr_de)

            # hu
            nodeStr_hu = tsl_hu.createElement('string')
            nodeStr_hu.setAttribute('name', str(row['android_key']))
            nodeStr_hu.appendChild(tsl_hu.createTextNode(str(row['Hu'])))

            tsl_hu_root.appendChild(nodeStr_hu)

    with open('./strings/android_strings_en.xml', 'w', encoding='utf-8') as fp:
        tsl_en.writexml(fp, indent='\t', addindent='\t', newl='\n', encoding="utf-8")
        print("EN strings exported")

    with open('./strings/android_strings_fr.xml', 'w', encoding='utf-8') as fp:
        tsl_fr.writexml(fp, indent='\t', addindent='\t', newl='\n', encoding="utf-8")
        print("FR strings exported")

    with open('./strings/android_strings_sp.xml', 'w', encoding='utf-8') as fp:
        tsl_sp.writexml(fp, indent='\t', addindent='\t', newl='\n', encoding="utf-8")
        print("SP strings exported")

    with open('./strings/android_strings_cn.xml', 'w', encoding='utf-8') as fp:
        tsl_cn.writexml(fp, indent='\t', addindent='\t', newl='\n', encoding="utf-8")
        print("CN strings exported")

    with open('./strings/android_strings_cz.xml', 'w', encoding='utf-8') as fp:
        tsl_cz.writexml(fp, indent='\t', addindent='\t', newl='\n', encoding="utf-8")
        print("CZ strings exported")

    with open('./strings/android_strings_nl.xml', 'w', encoding='utf-8') as fp:
        tsl_nl.writexml(fp, indent='\t', addindent='\t', newl='\n', encoding="utf-8")
        print("NL dutch strings exported")

    with open('./strings/android_strings_de.xml', 'w', encoding='utf-8') as fp:
        tsl_de.writexml(fp, indent='\t', addindent='\t', newl='\n', encoding="utf-8")
        print("DE strings exported")

    with open('./strings/android_strings_hu.xml', 'w', encoding='utf-8') as fp:
        tsl_hu.writexml(fp, indent='\t', addindent='\t', newl='\n', encoding="utf-8")
        print("HU strings exported")

