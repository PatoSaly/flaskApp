function show(id) {
    let elemGeneral = document.getElementById('valuesGeneral');
    let elemCpu = document.getElementById('valuesCpu');
    let elemMemory = document.getElementById('valuesMemory');

    if (id === 'valuesGeneral') {
        elemGeneral.style.visibility = "visible";
        elemCpu.style.visibility = "hidden";
        elemMemory.style.visibility = "hidden";
    } else if (id === 'valuesCpu') {
        elemCpu.style.visibility = "visible";
        elemGeneral.style.visibility = "hidden";
        elemMemory.style.visibility = "hidden";
    } else if (id === 'valuesMemory') {
       elemMemory.style.visibility = "visible";
        elemGeneral.style.visibility = "hidden";
        elemCpu.style.visibility = "hidden";
    }
}