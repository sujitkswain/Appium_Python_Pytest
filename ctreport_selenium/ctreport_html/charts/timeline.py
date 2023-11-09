def chart(tests):
    id_name_dict = {}
    min_li = []
    for test in tests:
        id_name_dict[test._id] = test._name
        duration = test._duration.split(':')
        hour = float(duration[0])
        min = float(duration[1])
        sec = float(duration[2]) + min * 60 + hour * 60 * 60
        min_li.append(sec)

    content = '''
        var dict= ''' + str(id_name_dict) + '''
        var timelinechart = new Chart(document.getElementById("timelinechart"), {
            type: 'line',
            data: {
                labels: ''' + str(list(id_name_dict.keys())) + ''',
                datasets: [
                    {
                        backgroundColor:"rgba(188, 216, 249,0.4)",
                        borderColor:"rgb(188, 216, 249)",
                        pointBackgroundColor: "rgba(188, 216, 249,0.6)",
                        pointBorderColor: "#000000",
                        pointStyle:"crossRot",
                        showLine:true,
                        data: ''' + str(min_li) + ''',
                        lineTension:0,
                    },
                ]
            },
            options: {
                legend: {
                    display: false
                },
                tooltips: {
                    callbacks: {
                        label: function(tooltipItem, data) {
                            var label ='';
                            label += Math.round(tooltipItem.yLabel * 100) / 100;
                            label +=' sec';
                            return label;
                        },
                        title: function(tooltipItem, data) {
                            var title ='';
                            title += dict[tooltipItem[0].xLabel];
                            return title;
                        }
                    }
                },
                onClick: function(evt,i) {
                    var activePoint = timelinechart.getElementAtEvent(evt)[0];
                    var data = activePoint._chart.data;
                    var datasetIndex = activePoint._datasetIndex;
                    var value = this.data.datasets[datasetIndex].data[activePoint._index];
                    e = i[0];
                    var id = this.data.labels[e._index];
                    console.log(id);
                    display_other_page();
                    filterSelection("all");
                    document.getElementById(id).scrollIntoView();
                }
            },
            
        });
    '''
    return content
