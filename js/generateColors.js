function getPalettesFromFirstInput(hexColor) {
    
    var secondaryColors = new Array();
    var url = "http://www.colourlovers.com/api/palettes/top?jsonCallback=?&format=json&hex=" + hexColor;

    $.ajax({
        // contentType: "application/json",
        dataType: 'jsonp',
        type: "GET",
        url: url,
        success: function(data) {
            $.each(data[0].colors, function(ind, item){
                secondaryColors.push(item);
            });
            // sketchy code ahead
            var i = 0;
            while (secondaryColors.length < 8) {
                secondaryColors.push(data[1].colors[i]);
                i = i+1;
            }
        }
    });
    

    return secondaryColors;
}

function getPalettesFromFirstInputForRandomAlg(hexColor) {
    
    var secondaryColors = new Array();
    var url = "http://www.colourlovers.com/api/palettes/top?jsonCallback=?&format=json&hex=" + hexColor;

    $.ajax({
        // contentType: "application/json",
        dataType: 'jsonp',
        type: "GET",
        url: url,
        success: function(data) {
            $.each(data, function(i, palette){
                $.each(palette.colors, function(j, color){
                    secondaryColors.push(color);
                });
            });
        }
    });

    return secondaryColors;
}