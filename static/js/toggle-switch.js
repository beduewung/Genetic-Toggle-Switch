
var layout1 = {
  title: {
    text:'mRNA',
    font: {
      family: 'Courier New, monospace',
      size: 24
    },
    xref: 'paper',
    x: 0.05,
  },
  xaxis: {
    title: {
      text: 'Time (iterations)',
      font: {
        family: 'Courier New, monospace',
        size: 18,
        color: '#7f7f7f'
      }
    },
  },
  yaxis: {
    title: {
      text: 'Concentration',
      font: {
        family: 'Courier New, monospace',
        size: 18,
        color: '#7f7f7f'
      }
    }
  }
};
var layout2 = {
  title: {
    text:'Proteins',
    font: {
      family: 'Courier New, monospace',
      size: 24
    },
    xref: 'paper',
    x: 0.05,
  },
  xaxis: {
    title: {
      text: 'Time (iterations)',
      font: {
        family: 'Courier New, monospace',
        size: 18,
        color: '#7f7f7f'
      }
    },
  },
  yaxis: {
    title: {
      text: 'Concentration',
      font: {
        family: 'Courier New, monospace',
        size: 18,
        color: '#7f7f7f'
      }
    }
  }
};
document.addEventListener("DOMContentLoaded", ready);

function ready(){
  var IPTG = false;
  var IPTS = false;

  Plotly.newPlot('graph1', [{
    y: [0],
    mode: 'lines',
    line: {color: '#80CAF6'},
    name: 'mL'
  }, {
    y: [0],
    mode: 'lines',
    line: {color: '#DF56F1'},
    name: 'mT'
  }], layout1);

  Plotly.newPlot('graph2', [{
    y: [0],
    mode: 'lines',
    line: {color: '#80CAF6'},
    name: 'pL'
  }, {
    y: [0],
    mode: 'lines',
    line: {color: '#DF56F1'},
    name: 'pT'
  }], layout2);
  
  var cnt = 0;
  var screen = document.getElementById("screen")
  var interval = setInterval(function() {

    const Http = new XMLHttpRequest();
    const url=`http://127.0.0.1:5000/get_data?iptg=${IPTG}&ipts=${IPTS}`;
    
    Http.open("GET", url);
    Http.send();

    Http.onreadystatechange = (e) => {
      // console.log("Response",Http.response);
      
      var data = JSON.parse(Http.response)
      Plotly.extendTraces('graph1', {
        y: [[data["mL"]], [data["mT"]]]
      }, [0, 1])

      Plotly.extendTraces('graph2', {
        y: [[data["pL"]], [data["pT"]]]
      }, [0, 1])

      var blue = Math.floor((data["mL"] / data["mT"]) * 255)
      var red = Math.floor((data["mT"] / data["mL"]) * 255)
      screen.style.backgroundColor = `rgba(${red}, 0, ${blue}, .8)`
      console.log(`rgb(${red}, 0, ${blue})`);
      

    }}, 50);

  cb1 = document.getElementById("checkbox1")
  cb2 = document.getElementById("checkbox2")
  btn1 = document.getElementById("button-1")
  btn2 = document.getElementById("button-2")

  cb1.addEventListener( 'change', (e) => {
    if(e.target.checked) {
      IPTG = true
    } else {
      IPTG = false
    }
  })
  cb2.addEventListener( 'change', (e) => {
    
    if(e.target.checked) {
      IPTS = true
    } else {
      IPTS = false
    }
  })

  btn1.addEventListener('click', (e) => {
    console.log("btn 1");
    cb1.checked = true;
    IPTG = true
    setTimeout(() => {
      cb1.checked = false;
      IPTG = false
    }, 1000)

  })

  btn2.addEventListener('click', (e) => {
    console.log("btn 2");
    cb2.checked = true;
    IPTS = true
    setTimeout(() => {
      cb2.checked = false;
      IPTS = false
    }, 1000)

  })



}