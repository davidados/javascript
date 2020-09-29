
const slogans = [
    'Impossible is nothing',
    'Stronger than dirt',
    'Belong anywhere',
    'I can’t believe I ate the whole thing',
    'You’re in good hands',
    'Don’t leave home without it',
    'Think different',
    'We try harder',
    'The ultimate driving machine',
    'The quicker picker-upper',
    'Have it your way',
    'Mmm, mmm good!',
    'What’s in your wallet?',
    'The heartbeat of America',
    'Does she or doesn’t she?',
    'Open happiness',
    'A diamond is forever',
    'The happiest place on earth',
    'America runs on Dunkin’',
    'It keeps going… and going… and going',
    'Move fast and break things',
    'When it absolutely, positively has to be there overnight',
    'They’re grrrrrrreat!',
    'Is it in you?',
    'So easy a caveman can do it',
    'We bring good things to life',
    'Don’t be evil',
    'Nothing runs like a deer',
    'Every kiss begins with Kay',
    'Finger lickin’ good',
    'The relentless pursuit of perfection',
    'Because you’re worth it',
    'Betcha can’t eat just one',
    'Melts in your mouth, not in your hands',
    'Good to the last drop',
    'I’m lovin’ it',
    'When it rains, it pours',
    'Just do it',
    'The choice of a new generation',
    'Snap! Crackle! Pop!',
    'Taste the rainbow',
    'Obey your thirst',
    'Takes a licking and keeps on ticking',
    'Trix are for kids',
    'Fly the friendly skies',
    'What can brown do for you?',
    'Can you hear me now?',
    'Think small',
    'Where’s the beef?',
    'The breakfast of champions']


function changeText() {
    let randomIndex = Math.floor(Math.random() * (slogans.length - 1) + 1);
    document.getElementById("lizard-title").innerHTML = slogans[randomIndex]
    document.getElementById("chimney-title").innerHTML = slogans[randomIndex]
}




