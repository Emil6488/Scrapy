
$(document).ready(function(){
    $('#area').on('change', function() {
        switch (this.value) {
            case "losangeles":
                cleanSubAreaSelection();
                setSubAreaLosAngeles();
                console.log("Los Angeles sub areas are added");
                break;
            case "SF bayArea":
                cleanSubAreaSelection();
                setSubAreaSanFrancisko();
                console.log("San Francisco is selected");
                break;
            default:
              console.log("Sorry, we are out of " + expr + ".");
          }
    });
});
function setSubAreaLosAngeles(){
    $("#subarea").append(new Option("all los angeles", "1"));
    $("#subarea").append(new Option("SF valley", "sfv"));
    $("#subarea").append(new Option("antelope valley", "ant"));
    $("#subarea").append(new Option("central LA", "lac"));
    $("#subarea").append(new Option("long beach", "lgb"));
    $("#subarea").append(new Option("san gabriel valley", "sgv"));
    $("#subarea").append(new Option("westside-southbay", "wst"));
}

function setSubAreaSanFrancisko(){
    $("#subarea").append(new Option("all SF bay area", "1"));
    $("#subarea").append(new Option("east bay", "eby"));
    $("#subarea").append(new Option("north bay", "nby"));
    $("#subarea").append(new Option("peninsula", "pen"));
    $("#subarea").append(new Option("san francisco", "sfc"));
    $("#subarea").append(new Option("santa cruz", "scz"));
    $("#subarea").append(new Option("south bay", "sby"));

}

function cleanSubAreaSelection(){
    $("#subarea").empty();
}