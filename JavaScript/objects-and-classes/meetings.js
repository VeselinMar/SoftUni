function solve(arrayOfStrings) {
    let meetingSchedule = {};

    for(element of arrayOfStrings) {
        let [day, firstName] = element.split(' ');

        if(day in meetingSchedule) {
            console.log(`Conflict on ${day}!`);
        } else {
            meetingSchedule[day] = firstName
            console.log(`Scheduled for ${day}`)
        }
    }

    for(element in meetingSchedule) {
        console.log(`${element} -> ${meetingSchedule[element]}`)
    }
}

solve(['Monday Peter',
'Wednesday Bill',
'Monday Tim',
'Friday Tim'])

solve(['Friday Bob',
'Saturday Ted',
'Monday Bill',
'Monday John',
'Wednesday George'])