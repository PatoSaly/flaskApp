function show(id) {
    if (id === 'valuesGeneral') {
        document.getElementById('valuesGeneral').style.visibility = "visible";
        document.getElementById('valuesCpu').style.visibility = "hidden";
        document.getElementById('valuesMemory').style.visibility = "hidden";
    } else if (id === 'valuesCpu') {
        document.getElementById('valuesCpu').style.visibility = "visible";
        document.getElementById('valuesGeneral').style.visibility = "hidden";
        document.getElementById('valuesMemory').style.visibility = "hidden";
    } else if (id === 'valuesMemory') {
        document.getElementById('valuesMemory').style.visibility = "visible";
        document.getElementById('valuesGeneral').style.visibility = "hidden";
        document.getElementById('valuesCpu').style.visibility = "hidden";
    }
}