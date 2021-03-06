#!/usr/bin/env python2
# -*- coding: utf-8 -*-

#-:-:-:-:-:-:-:-:-:-:-:-:#
#    TIDoS Framework     #
#-:-:-:-:-:-:-:-:-:-:-:-:#

#Author: @_tID (Modified version from wascan)
#This module requires TIDoS Framework
#https://github.com/the-Infected-Drake/TIDoS-Framework

from re import search,I 

def sophos(headers,content):
	detect = False
	detect |= search(r"Powered by UTM Web Protection",content) is not None
	if detect : 
		return "UTM Web Protection (Sophos)"
