
$(document).ready(function(){
    console.log("Hello World")
    $('#area').on('change', function() {
        switch (this.value) {
            case "losangeles":
                cleanSubAreaSelection();
                setSubAreaLosAngeles();
                console.log("Los Angeles sub areas are added");
                break;
            case "bakersfield":
                cleanSubAreaSelection();
                console.log("Bakersfield is selected");
                break;
            case "fresno":
                cleanSubAreaSelection();
                console.log("Fresno is selected");
                break;
            case "hanford":
                console.log("Cherries are $3.00 a pound.");
                break;
            case "imperial":
            case "inlandempire":
            case "lasvegas":
            case "orangecounty":
                console.log("Mangoes and papayas are $2.79 a pound.");
                break;
            case "palmsprings":
                console.log("Mangoes and papayas are $2.79 a pound.");
                break;
            case "sandiego":
                console.log("Mangoes and papayas are $2.79 a pound.");
                break;
            case "slo":
                console.log("Mangoes and papayas are $2.79 a pound.");
                break;
            case "santabarbara":
                console.log("Mangoes and papayas are $2.79 a pound.");
                break;
            case "santamaria":
                console.log("Mangoes and papayas are $2.79 a pound.");
                break;
            case "ventura":
                console.log("Mangoes and papayas are $2.79 a pound.");
                break;
            case "visalia":
                console.log("Mangoes and papayas are $2.79 a pound.");
                break;
            case "yuma":
                setSubAreaLosAngeles()
                console.log("Yuma selected.");
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

function cleanSubAreaSelection(){
    $("#subarea").empty();
}