from flask import Flask, jsonify


app = Flask(__name__)


dataset = [
    "How can we design a more efficient transportation system for urban areas?",
"What improvements can be made to home appliances to increase energy efficiency?",
"How can we optimize water usage in households?",
"What innovative solutions can reduce plastic waste in everyday products?",
"How can engineering improve food preservation techniques to reduce food waste?",
"What advancements can be made in renewable energy sources for residential use?",
"How can engineering address accessibility issues for people with disabilities in public spaces?",
"What technologies can enhance home security systems?",
"How can engineering help improve air quality in urban environments?",
"What strategies can be implemented to make public transportation more accessible and convenient?",
"How can engineering contribute to more sustainable agriculture practices?",
"What improvements can be made to infrastructure to withstand natural disasters more effectively?",
"How can engineering enhance communication systems during emergencies?",
"What advancements can be made in medical devices to improve healthcare at home?",
"How can engineering improve the efficiency of recycling processes?",
"What technologies can assist in managing and reducing household waste?",
"How can engineering address challenges related to water scarcity in certain regions?",
"What innovations can improve the durability of roads and reduce maintenance costs?",
"How can engineering contribute to reducing the environmental impact of construction projects?",
"What improvements can be made to public parks and recreational areas using engineering principles?",
"How can engineering enhance the efficiency of public lighting systems?",
"What advancements can be made in sustainable urban design to create more livable cities?",
"How can engineering help mitigate the effects of climate change on coastal communities?",
"What technologies can improve indoor air quality in buildings?",
"How can engineering contribute to the development of smart cities with interconnected infrastructure?",
"What innovations can improve the safety of playgrounds and recreational equipment?",
"How can engineering address challenges related to waste management in developing countries?",
"What advancements can be made in water purification technology for household use?",
"How can engineering help reduce noise pollution in urban areas?",
"What improvements can be made to public transportation to make it more environmentally friendly?",
"How can engineering enhance the efficiency of heating and cooling systems in buildings?",
"What technologies can assist in monitoring and conserving natural resources?",
"How can engineering contribute to the development of sustainable packaging materials?",
"What innovations can improve the accessibility of public buildings for people with disabilities?",
"How can engineering help improve disaster preparedness and response efforts?",
"What advancements can be made in waste-to-energy technology?",
"How can engineering address challenges related to food distribution and storage?",
"What improvements can be made to urban drainage systems to prevent flooding?",
"How can engineering enhance the safety of bridges and other infrastructure?",
"What technologies can assist in detecting and mitigating air pollution levels?",
"How can engineering contribute to the development of affordable housing solutions?",
"What innovations can improve the efficiency of public transportation systems?",
"How can engineering help reduce the environmental impact of manufacturing processes?",
"What advancements can be made in sustainable fashion and textile production?",
"How can engineering address challenges related to sustainable water management?",
"What improvements can be made to waste collection and disposal systems?",
"How can engineering enhance the resilience of buildings to earthquakes and other natural disasters?",
"What technologies can assist in monitoring and controlling air and water pollution?",
"How can engineering contribute to the development of green building materials?",
"What innovations can improve the safety and efficiency of public infrastructure maintenance?",
"How can engineering help improve access to clean drinking water in rural areas?",
"What advancements can be made in renewable energy storage technology?",
"How can engineering address challenges related to urban sprawl and land use?",
"What improvements can be made to transportation infrastructure to reduce traffic congestion?",
"How can engineering enhance the efficiency of waste sorting and recycling processes?",
"What technologies can assist in monitoring and managing natural disasters?",
"How can engineering contribute to the development of sustainable transportation options?",
"What innovations can improve the safety and accessibility of public spaces for all demographics?",
"How can engineering help reduce energy consumption in residential and commercial buildings?",
"What advancements can be made in desalination technology to address water scarcity?",
"How can engineering address challenges related to electronic waste management?",
"What improvements can be made to irrigation systems to conserve water in agriculture?",
"How can engineering enhance the efficiency of public lighting systems?",
"What technologies can assist in monitoring and mitigating the effects of climate change?",
"How can engineering contribute to the development of more efficient and sustainable farming practices?",
"What innovations can improve the safety and accessibility of transportation for people with disabilities?",
"How can engineering help reduce the environmental impact of deforestation?",
"What advancements can be made in renewable energy generation from sources like wind and solar?",
"How can engineering address challenges related to soil erosion and degradation?",
"What improvements can be made to wastewater treatment plants to reduce pollution?",
"How can engineering enhance the resilience of coastal infrastructure to sea-level rise?",
"What technologies can assist in monitoring and managing wildlife populations?",
"How can engineering contribute to the development of sustainable fishing practices?",
"What innovations can improve the safety and efficiency of mining operations?",
"How can engineering help reduce the environmental impact of oil and gas extraction?",
"What advancements can be made in carbon capture and storage technology?",
"How can engineering address challenges related to invasive species management?",
"What improvements can be made to agricultural machinery to increase efficiency and reduce environmental impact?",
"How can engineering enhance the sustainability of forestry practices?",
"What technologies can assist in monitoring and protecting biodiversity?",
"How can engineering contribute to the development of sustainable tourism practices?",
"What innovations can improve the safety and efficiency of renewable energy installations?",
"How can engineering help reduce the environmental impact of urbanization?",
"What advancements can be made in green chemistry to develop more eco-friendly products?",
"How can engineering address challenges related to soil contamination and remediation?",
"What improvements can be made to transportation infrastructure to accommodate electric vehicles?",
"How can engineering enhance the efficiency of water distribution systems?",
"What technologies can assist in monitoring and managing air quality in urban areas?",
"How can engineering contribute to the development of sustainable waste management practices?",
"What innovations can improve the safety and efficiency of disaster response and recovery efforts?",
"How can engineering help reduce the environmental impact of industrial processes?",
"What advancements can be made in sustainable forestry management?",
"How can engineering address challenges related to plastic pollution in oceans and waterways?",
"What improvements can be made to building materials to increase durability and sustainability?",
"How can engineering enhance the efficiency of public transportation systems through automation?",
"What technologies can assist in monitoring and managing noise pollution?",
"How can engineering contribute to the development of sustainable supply chains?",
"What innovations can improve the safety and efficiency of renewable energy transmission?",
"How can engineering help reduce the environmental impact of shipping and logistics?",
"What advancements can be made in urban planning to create more sustainable and resilient cities?"

]

# Define API endpoint to get all prompts
@app.route('/prompts', methods=['GET'])
def get_prompts():
    return jsonify(dataset)


@app.route('/prompts/<int:index>', methods=['GET'])
def get_prompt(index):
    if index < 0 or index >= len(dataset):
        return jsonify({'error': 'Invalid index'}), 404
    return jsonify(dataset[index])


if __name__ == '__main__':
    app.run(debug=True)