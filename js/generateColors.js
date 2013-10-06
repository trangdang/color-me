function getPalettesFromFirstInput(hexColor) {
    var url = "http://www.colourlovers.com/api/palettes/top?jsonCallback=?&format=json&hex=";
    return $.ajax({
        // contentType: "application/json",
        dataType: 'jsonp',
        type: "GET",
        url: url + hexColor,
        success: function(data) {
            processData(data);
        }
    });
}

function processData(data) {
    var secondaryColors = new Array();

    $.each(data[0].colors, function(ind, item){
        secondaryColors.push(item);
    });
    // sketchy code ahead
    var i = 0;
    while (secondaryColors.length < 8) {
        secondaryColors.push(data[1].colors[i]);
        i = i+1;
    }        

    $.each(secondaryColors, function(i, item){
        $('body').append(item);
    });
}

function getPalettesFromFirstInputForRandomAlg(hexColor) {
    var url = "http://www.colourlovers.com/api/palettes/top?jsonCallback=?&format=json&hex=";
    $.ajax({
        // contentType: "application/json",
        dataType: 'jsonp',
        type: "GET",
        url: url + hexColor,
        success: function(data) {

            var secondaryColors = new Array();
            
            $.each(data, function(i, palette){
                $.each(palette.colors, function(j, color){
                    if (color !== hexColor) {
                        secondaryColors.push(color);
                    };
                });
            });

            algorithmitizeData(secondaryColors);
        }
    });
}

function algorithmitizeData(array) {
    console.log(array);
    $.ajax({
        type: "POST",
        url: "http://127.0.0.1:5000/get-colors",
        data: JSON.stringify({content: array}),
        dataType: "json",
        contentType:"application/json",
        success: function(data) {
            // dispAlgData(data);
            console.log(data);
        }
    });
}

function dispAlgData(data) {
    alert('sucess');
}