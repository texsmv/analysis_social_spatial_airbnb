
$.get('paris.geojson', function (parisJson) {
    
    echarts.registerMap('paris', parisJson);
    myChartMapa.setOption(
        
        {geo: {
        map: 'paris',
        },
        tooltip: {
            trigger: 'item',
            formatter: function (params, ticket, callback) {
                return "Cluster: " + params.data[2]
            }
        },
        })   
});



$.get('data.json',function(datajson){
    
    myChartMapa.setOption({
        
        visualMap: [
        // {
        //     min: 0,
        //     max: datajson.reduce( (prev, current) => (prev > current.price ) ? prev : current.price ),
        //     splitNumber: 6,
        //     // precision: 2,
        //     // categories : [ "0" , "1", "2" ],
        //     color: ['#d94e5d','#eac736','#50a3ba'],
        //     textStyle: {
        //         color: '#000'
        //     }
        // },
        {
            // min: 0,
            // max: 3,
            // splitNumber: 3,
            precision: 2,
            categories : [ "0" , "1", "2" ],
            align:'right',
            color: ['#d94e5d','#eac736','#50a3ba'],
            textStyle: {
                color: '#000'
            }
        },
    
    ],

        series: [
    //     {
    //     type: 'heatmap',
    //     coordinateSystem: 'geo',
    //     data: datajson.map( dato => [dato.longitude,dato.latitude, dato.price ]),
    //     // data: datajson.map( dato => [dato.longitude,dato.latitude,Math.floor(dato.label).toString() ]),
    //     // symbolSize: 3,
    //     blursize: 5,
    //     itemStyle: {
    //         emphasis: {
    //             borderColor: '#000',
    //             borderWidth: 1
    //         }
    //     }
    // },

        {
            type: 'scatter',
            coordinateSystem: 'geo',
            // data: datajson.map( dato => [dato.longitude,dato.latitude, dato.price ]),
            data: datajson.map( dato => [dato.longitude,dato.latitude,Math.floor(dato.label).toString() ]),
            symbolSize: 3,
           
            itemStyle: {
                emphasis: {
                    borderColor: '#000',
                    borderWidth: 1
                }
            }
        }
    
    
    ]
    })

  
});