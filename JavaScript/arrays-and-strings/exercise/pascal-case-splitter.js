function solve(inputString) {
    const words = inputString.split(/(?=[A-Z])/);
    return words.join(", ");
}

solve('SplitMeIfYouCanHaHaYouCantOrYouCan');
solve('HoldTheDoor');
solve('ThisIsSoAnnoyingToDo');