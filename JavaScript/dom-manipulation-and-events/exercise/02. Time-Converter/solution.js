function attachEventsListeners() {
    //buttons
    const convertDaysButton = document.getElementById("daysBtn");
    const convertHoursButton = document.getElementById("hoursBtn");
    const convertMinutesButton = document.getElementById("minutesBtn");
    const convertSecondsButton = document.getElementById("secondsBtn");
    //fields
    const daysField = document.getElementById("days");
    const hoursField = document.getElementById("hours");
    const minutesField = document.getElementById("minutes");
    const secondsField = document.getElementById("seconds");
    // click days
    convertDaysButton.addEventListener('click', () => {
        const days = parseFloat(daysField.value);

        hoursField.value = days * 24;
        minutesField.value = days * 24 * 60;
        secondsField.value = days * 24 * 60 * 60;
    })
    // click hours
    convertHoursButton.addEventListener('click', () => {
        const hours = parseFloat(hoursField.value);

        daysField.value = hours / 24;
        minutesField.value = hours * 60;
        secondsField.value = hours * 60 * 60;
    })
    // click minutes
    convertMinutesButton.addEventListener('click', () => {
        const minutes = parseFloat(minutesField.value);

        daysField.value = minutes / 60 / 24;
        hoursField.value = minutes / 60;
        secondsField.value = minutes * 60;
    })
    // click seconds
    convertSecondsButton.addEventListener('click', () => {
        const seconds = parseFloat(secondsField.value);

        daysField.value = seconds / 60 / 60 / 24;
        hoursField.value = seconds / 60 / 60;
        minutesField.value = seconds / 60;
    })
}