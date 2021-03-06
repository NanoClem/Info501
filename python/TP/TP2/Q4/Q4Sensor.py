# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 19:47:50 2017

@author: lfoul
"""

import http
import urllib

class Sensor:
    # Constructor
    def __init__(self, url, label, thresholds):
        self.url = url
        self.label = label 
        self.thresholds = thresholds
    
    # Setters
    def setGeneralConfiguration(self, generalConfiguration):
        self.generalConfiguration = generalConfiguration
    
    # Getters
    def getGeneralConfiguration(self):
        return self.generalConfiguration       

    def getLabel(self):
        return self.label
                     
    # Checks if the connection to the sensor is set
    def isConnectedToUrl(self):
        try:
            self.request = urllib.request.urlopen(self.url)
        except OSError:
            return False
        else:
            return self.request.getcode() == http.HTTPStatus.OK

    # Reads the sensor
    def read(self):
        if self.isConnectedToUrl():
            return self.request.read().decode('utf-8')
        else:
            return None
        
    # Gets the transformed value
    def getTransformedValue(self):
        sensValue  = float(self.read())      # valeur du sensor
        result     = 0                       # résultat après normalisation
        Smin       = self.thresholds[0]
        Sneutral   = self.thresholds[1]
        Smax       = self.thresholds[2]
        
        # NORMALISATION DE LA VALEUR DU SENSOR
        if(sensValue < Sneutral):
            result = (sensValue - Sneutral) / (Sneutral - Smin)
        else :
            result = (sensValue - Sneutral) / (Smax - Sneutral)
            
        # ECRETAGE
        if(result > 1):
            result = 1
        elif(result < -1):
            result = -1
            
        return result
        
        
        
        
                   
        