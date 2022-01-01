//
//  ContentView.swift
//  Shared
//
//  Created by Aidan Donaghey on 12/30/21.
//

import SwiftUI
import SwiftMQTT

struct ContentView: View {
//    var client = MQTTManager()
    let topicStart = "/rasplights/"
    let mqttSession = MQTTSession(
        host: "192.168.1.127",
        port: 1883,
        clientID: "swift", // must be unique to the client
        cleanSession: true,
        keepAlive: 15,
        useSSL: false
    )
    let columnLayout = Array(repeating: GridItem(), count: 10)
    @State private var selectedColor = Color.cyan
    let allColors: [Color] = [.cyan,.blue,.indigo]
    
    
    var body: some View {
        
        VStack{
            Text("Selected Option")
                .font(.body)
                .fontWeight(.semibold)
                .foregroundColor(selectedColor)
                .padding(10)
            OptionCard(color: Color.red, title: "Turn on ", colorOption: selectedColor,mqqtSession: mqttSession)
            OptionCard(color: Color.blue, title: "Turn on ", colorOption: selectedColor,mqqtSession: mqttSession)
            OptionCard(color: Color.green, title: "Turn on ", colorOption: selectedColor,mqqtSession: mqttSession)
            OptionCard(color: Color.black, title: "Turn off ", colorOption: selectedColor,mqqtSession: mqttSession)
        
        }
    }
}


struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        Group {
            ContentView()
        }
    }
}


struct CardModifier: ViewModifier {
    let color: Color
    var mqqtSession: MQTTSession
    func body(content: Content) -> some View {
        return content
            .cornerRadius(20)
            .shadow(color: Color.black.opacity(0.2), radius: 20, x: 0, y: 0)
            .modifier(Track(eventName: color.description, mqqtSession: mqqtSession))
    }
}

struct Track: ViewModifier {
    let eventName: String
    let mqqtSession: MQTTSession
    func body(content: Content) -> some View {
        return content.simultaneousGesture(TapGesture().onEnded({
            print(self.eventName)
//            Connecting First on Click
            
            let json = ["key" : "value"]
            let data = try! JSONSerialization.data(withJSONObject: json, options: .prettyPrinted)
            let topic = "off"
            mqqtSession.publish(data, in: topic, delivering: .atLeastOnce, retain: false) { error in
                if error == .none {
                    print("Published data in \(topic)!")
                } else {
                    print(error.description)
                }
            }
        }))
    }
}



struct OptionCard: View {
    
    var color: Color
    var title: String
    var colorOption: Color
    var mqqtSession: MQTTSession
    
    var body: some View {
//        let tap = TapGesture()
//                   .onEnded { _ in
//                       print("Square Tapped " + color.description)
//                   }
        HStack(alignment: .center) {
            Rectangle()
                .fill(color)
                .aspectRatio(contentMode: .fit)
                .padding(.all, 20)
                .frame(width: 100)
                
            
            Spacer()
            VStack(alignment: .trailing) {
                Text(title + color.description)
                    .font(.system(size: 26, weight: .bold, design: .default))
                    .foregroundColor(.white)
            }.padding(.trailing,40)
            
        }
        .frame(maxWidth: .infinity, alignment: .center)
        .background(Color(red: 32/255, green: 36/255, blue: 38/255))
        .modifier(CardModifier(color: color,mqqtSession: mqqtSession))
//        .modifier(Track(eventName: color.description + "tapped!"))

        .padding(.all, 10)
    }
}
