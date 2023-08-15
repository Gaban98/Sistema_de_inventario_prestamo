function updateClock() {
    const currentTime = new Date();
    const hours = currentTime.getHours();
    const minutes = currentTime.getMinutes();

    const timeString = hours + ":" + minutes ;
    document.getElementById("current-time").innerText = timeString;
}

// Actualizar la hora cada segundo
setInterval(updateClock, 1000);
