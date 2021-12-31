//
//  ContentView.swift
//  Shared
//
//  Created by Aidan Donaghey on 12/30/21.
//

import SwiftUI

struct ContentView: View {
    var client = MQTTManager()
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
            OptionCard(color: Color.red, title: "Turn on ", colorOption: selectedColor,client: client)
            OptionCard(color: Color.blue, title: "Turn on ", colorOption: selectedColor,client: client)
            OptionCard(color: Color.green, title: "Turn on ", colorOption: selectedColor,client: client)
            OptionCard(color: Color.black, title: "Turn off ", colorOption: selectedColor,client: client)
        
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
    let client: MQTTManager
    func body(content: Content) -> some View {
        return content
            .cornerRadius(20)
            .shadow(color: Color.black.opacity(0.2), radius: 20, x: 0, y: 0)
            .modifier(Track(eventName: color.description, client: client))
    }
}

struct Track: ViewModifier {
    let eventName: String
    let client: MQTTManager

    func body(content: Content) -> some View {
        return content.simultaneousGesture(TapGesture().onEnded({
            client.publish(topic: "/raspights/" + eventName, message: "10")
            print(self.eventName)
        }))
    }
}



struct OptionCard: View {
    
    var color: Color
    var title: String
    var colorOption: Color
    var client : MQTTManager
    
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
        .modifier(CardModifier(color: color, client: client))
//        .modifier(Track(eventName: color.description + "tapped!"))

        .padding(.all, 10)
    }
}
