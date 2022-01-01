//
//  LightsAPI.swift
//  LightController
//
//  Created by Aidan Donaghey on 12/31/21.
//

import Foundation
import CocoaMQTT


class MQTTManager{
    private var mqtt: CocoaMQTT
    private var host: String
    private var clientID: String
    init(){
        self.host = "192.168.1.127"
        self.clientID = "CocoaMQTT-" + String(ProcessInfo().processIdentifier)
        self.mqtt = CocoaMQTT(clientID: clientID, host: self.host , port: 1883)
//        self.mqtt.username = "test"
//        self.mqtt.password = "public"
//        self.mqtt.keepAlive = 60
        print("The MQTT is intialised")
        self.connect()
        self.publishOn()
    }
    
    func connect(){
        print("Trying to connect.....")
        self.mqtt.connect()
        print("Connected.....")
    }
    
    func publish(topic :String, message: String){
        self.mqtt.publish(topic, withString: message)
    }
    
    func publishOn(){
        print("Trying to Publish.....")
        self.mqtt.publish("/rasplights/on" , withString: "message", qos: .qos1, retained: false)
        print("Published...")
    }
    
}

