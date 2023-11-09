from ctreport_selenium.utility_classes import Severity


def chart(count):
    pass_ = str(count[0])
    fail_ = str(count[1])
    label = Severity.BLOCKER.capitalize()
    content = '''
        new Chart(document.getElementById("assertionchart"), {
        type: 'bar',
        data: {
          labels: ["''' + label + '''"],
          datasets: [
            {
              label: "Passed",
              backgroundColor: "#00AF00",
              data: [''' + str(pass_) + ''']
            }, {
              label: "Failed",
              backgroundColor: "#F7464A",
              data: [''' + str(fail_) + ''']
            }
          ]},
        options: {
          title: {
            fontSize:20,
            display: false,
            text: 'Group under Priority'
          },
          legend: {
            position:'bottom'
          },
          scales: {
            xAxes: [{
                barThickness : 40,
                barPercentage: 19,			
            }],
            yAxes: [{
                display: true,
                ticks: {
                    display: false,
                    maxTicksLimit: 6,
                    precision:0,
				}
            }],
          }
        }
    });
    '''
    return content
