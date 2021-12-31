//
//  ContentView.swift
//  Shared
//
//  Created by Aidan Donaghey on 12/30/21.
//

import SwiftUI

struct ContentView: View {
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
            OptionCard(color: Color.red, title: "Turn on ", price: 11.99)
            OptionCard(color: Color.blue, title: "Turn on ", price: 11.99)
            OptionCard(color: Color.green, title: "Turn on ", price: 11.99)
            OptionCard(color: Color.gray, title: "Choose Color", price: 11.99)
        
        }
    }
}


struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}


struct CardModifier: ViewModifier {
    func body(content: Content) -> some View {
        content
            .cornerRadius(20)
            .shadow(color: Color.black.opacity(0.2), radius: 20, x: 0, y: 0)
    }
    
}

struct OptionCard: View {
    
    var color: Color
    var title: String
    var price: Double
    
    var body: some View {
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
        .modifier(CardModifier())
        .padding(.all, 10)
    }
}
