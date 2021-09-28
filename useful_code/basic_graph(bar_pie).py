# bar graph
fifa2019['Preferred Foot'].value_count().plot(kind = 'bar')

# pie graph
fifa2019['Preferred Foot'].value_count().plot(kind = 'pie', autopct = '%1.f% %')
