def chart(status):
    content = '''
        var statuschart=new Chart(document.getElementById("statuschart"), {
            type: 'doughnut',
            data: {
                labels: ["Passed", "Failed", "Skipped","Broken"],
                datasets: [{
                    label: "Population (millions)",
                    backgroundColor: ["#00AF00", "#F7464A","#1E90FF","#aaa"],
                      data: [''' + str(status[0]) + ''',''' + str(status[1]) + ''',''' + \
              str(status[2]) + ''',''' + str(status[3]) + ''']
                }]	
            },
            options: {
                responsive: true,
                cutoutPercentage: 80,
                title: {
                    display: false,
                    text: 'Status'
                  },
                legend: {
                    position:'right',
                },
                onClick:function(e){
                    try {
                        var dict = {
                          0: "passed",
                          1: "failed",
                          2: "skipped",
                          3: "broken",
                        };
                        var activePoints = statuschart.getElementsAtEvent(e);
                        var selectedIndex = activePoints[0]._index;
                        var status=selectedIndex;
                        console.log(status);
                        display_other_page();
                        filterSelection(dict[status]);
                        toast_message(dict[status]);
                    }
                    catch(err) {}
                }
            },
        });
    '''
    # return content
    content1 = '''
    $(function(){
			Chart.pluginService.register({
			  beforeDraw: function(chart) {
				var width = chart.chart.width,
					height = chart.chart.height,
					ctx = chart.chart.ctx,
					type = chart.config.type;

				if (type == 'doughnut')
				{
                    var percent = Math.round((chart.config.data.datasets[0].data[0] * 100)/
                                            (chart.config.data.datasets[0].data[0]+
                                            chart.config.data.datasets[0].data[1]+
                                            chart.config.data.datasets[0].data[2]+
                                            chart.config.data.datasets[0].data[3]));
						var oldFill = ctx.fillStyle;
				  var fontSize = ((height - chart.chartArea.top) / 100).toFixed(2);
				  
				  ctx.restore();
				  ctx.font = fontSize + "em sans-serif";
				  ctx.textBaseline = "middle"

				  var text = percent + "%",
					  textX = Math.round((width - ctx.measureText(text).width-100) / 2),
					  textY = (height + chart.chartArea.top) / 2;
						
				  ctx.fillStyle = chart.config.data.datasets[0].backgroundColor[0];
				  ctx.fillText(text, textX, textY);
				  ctx.fillStyle = oldFill;
				  ctx.save();
				}
			  }
			});

		var statuschart = new Chart(document.getElementById('statuschart'), {
		  type: 'doughnut',
		  data: {
					labels: ["Passed", "Failed", "Skipped","Broken"],
					datasets: [{
						label: "Population (millions)",
						backgroundColor: ["#00AF00", "#F7464A","#1E90FF","#aaa"],
						  data: [''' + str(status[0]) + ''',''' + str(status[1]) + ''',''' + \
               str(status[2]) + ''',''' + str(status[3]) + '''],
					}]	
				},
		  options: {
								responsive: true,
								cutoutPercentage: 80,
								title: {
									display: false,
									text: 'Status'
								  },
								legend: {
									position:'right',
								},
								onClick:function(e){
									try {
										var dict = {
										  0: "passed",
										  1: "failed",
										  2: "skipped",
										  3: "broken",
										};
										var activePoints = statuschart.getElementsAtEvent(e);
										var selectedIndex = activePoints[0]._index;
										var status=selectedIndex;
										display_other_page();
										filterSelection(dict[status]);
									}
									catch(err) {}
								}
							},
					});

				});
    '''
    return content1
