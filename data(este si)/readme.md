-------------------------------------------------------------------caracteristicas.csv----------------------------------------------------------------------------

tipos de dato

id                                  int64
room_type                           int64
price                               int64
calculated_host_listings_count      int64
latitude                          float64
longitude                         float64
host_response_time                  int64
host_response_rate                  int64
property_type                       int64
accommodates                        int64
bathrooms                         float64
bedrooms                          float64
beds                              float64
bed_type                            int64
cleaning_fee                      float64
cancellation_policy                 int64
Wifi                                int64
Heating                             int64
Kitchen                             int64
Essentials                          int64
Washer                              int64
Smoke detector                      int64
Hangers                             int64
Hair dryer                          int64
TV                                  int64
Iron                                int64
Shampoo                             int64
Laptop friendly workspace           int64
Hot water                           int64
Elevator                            int64
Family/kid friendly                 int64
Internet                            int64
Dryer                               int64
Refrigerator                        int64
Bed linens                          int64
Dishes and silverware               int64
Cable TV                            int64
Cooking basics                      int64
Coffee maker                        int64


columnas categoricas = ['host_response_time', 'room_type', 'bed_type', 'cancellation_policy', 'property_type']

    -->  host_response_time
    ['a few days or more' 'within a day' 'within a few hours' 'within an hour']

    -->  room_type
    ['Entire home/apt' 'Private room' 'Shared room']

    -->  bed_type
    ['Airbed' 'Couch' 'Futon' 'Pull-out Sofa' 'Real Bed']

    -->  cancellation_policy
    ['flexible' 'moderate' 'strict' 'strict_14_with_grace_period'
    'super_strict_30' 'super_strict_60']

    -->  property_type
    ['Aparthotel' 'Apartment' 'Bed and breakfast' 'Boat' 'Boutique hotel'
    'Cave' 'Condominium' 'Cottage' 'Dorm' 'Guest suite' 'Guesthouse' 'Hostel'
    'Hotel' 'House' 'Houseboat' 'In-law' 'Loft' 'Nature lodge' 'Other'
    'Serviced apartment' 'Tiny house' 'Townhouse' 'Treehouse' 'Villa']








-----------------------------------------------caracteristicas_coordinates_labels_2d.csv-----------------------------------------------


-Lo mismo que caracteristicas.csv mas latitud, longitud y label obtenido del clustering.
-Clustering hecho con dos dimensiones del vector caracteristica de 10 dimensiones
-Lo que era Dataframe2.csv





-----------------------------------------------caracteristicas_coordinates_labels_10d.csv------------------------------------------------


-Lo mismo que caracteristicas.csv mas latitud, longitud y label obtenido del clustering.
-Clustering hecho con las 10 dimensiones del vector caracteristica
-Lo que era Dataframe3.csv









-----------------------------------------------distancias_espaciales.csv---------------------------------------------------------
- columnas = poi_dists.csv,attraction_dists.csv,restaurant_dists.csv  (distancias a puntos de interes, atracciones, y restaurantes en un radio de 1.5km respectivamente) 
- longitude,latitude para plotear








---------------------------------------------- poi-categories--------------------------------------------------------------------
- Todas las subcategorias de paris-poi.csv estan dentro de la carpeta poi_categorias, las categorias son:
    ['Monument-Landmark', 'Historic Site', 'Road', 'Convention Center',
        'Medical Center', 'Embassy-Consulate', 'Hospital', 'Office',
        'Subway', 'Government Building', nan, 'Capitol Building',
        "Dentist's Office", 'Police Station', 'Bus Station',
        'Train Station', 'Rental Car Location', 'Boat or Ferry',
        'Light Rail', 'Train', 'Bike Rental-Bike Share', "Doctor's Office",
        'Fire Station', 'Library', 'Building', 'Meeting Room', 'Taxi',
        'City Hall', 'Parking', 'Bus Line', 'Emergency Room',
        'General Travel', 'Rest Area', 'Bridal Shop', 'Event Space',
        'Courthouse', 'Home (private)', 'Veterinarian', 'Park',
        'Laboratory', 'Pier', 'Eye Doctor', 'Moving Target',
        'Housing Development', 'Harbor-Marina', 'Miscellaneous Shop',
        'General College & University', 'Airport', 'Conference Room',
        'College Science Building', 'Travel Lounge', 'Hotel', 'Cemetery',
        'College Library', 'Gym', 'Student Center']

- Cada categoria posee los siguientes campos ['lat', 'lng', 'name']








-------------------------------------------lugares_turisticos.csv--------------------------------------------------------------
- 28 mejores lugares turisticos de Paris(tuve que crearlo)
- tiene los siguientes atributos: name,stars,n_reviews,lat,lng
- n_reviews y stars los saque de google maps








--------------------------------------------museos.csv--------------------------------------------------------------------
- Museos de Paris con los siguientes atributos name,lat,lng





--------------------------------------------------------------------------------------------------------------------------