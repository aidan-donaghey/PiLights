//
//  LightsAPI.swift
//  LightController
//
//  Created by Aidan Donaghey on 12/31/21.
//

import Foundation
import CocoaMQTT


class MQTTManager{
    private var mqttClient: CocoaMQTT?
    private var host: String!
    private var topic: String!
    
    init(){
        self.host = "192.168.1.127"
        let clientId = "CocoaMQTT"
        mqttClient = CocoaMQTT(clientID:clientId, host: host, port:1883)
        print("The MQTT is intialised")
        self.connect()
    }
    
    func connect(){
        if let success = mqttClient?.connect(), success {
            print("connected Sucessfully")
        }
    }
    
    func publish(topic :String, message: String){
        mqttClient?.publish(topic, withString: message)
    }
    
}

