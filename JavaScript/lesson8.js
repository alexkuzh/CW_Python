// class Clock {
//     constructor({ template }) {
//         this.template = template;
//     }
//
//     render(){
//         let date = new Date();
//         let hours = date.getHours();
//         if (hours < 10) hours = '0' + hours;
//
//         let mins = date.getMinutes();
//         if (mins < 10) mins = '0' + mins;
//
//         let secs = date.getSeconds();
//         if (secs < 10) secs = '0' + secs;
//
//         let output = this.template
//             .replace('h',hours)
//             .replace('h',hours)
//             .replace('m',mins)
//             .replace('s',secs);
//
//         console.log(output)
//     }
//
//     start(){
//         this.render();
//         this.timer = setInterval(() => this.render(),1000)
//     }
//
//     stop(){
//         clearInterval(this.timer)
//     }
//
// }
//
// clock1 = new Clock({template: 'hh:m:s'})
// clock1.start()
//
// class Planet(name, galaxy,
//                 numberOfMoons, weight)
// {
//     this.name = name;
//     this.galaxy = galaxy;
//     this.numberOfMoons = numberOfMoons;
//     this.weight = weight;
//
//     this.message = function(name){
//         return 'hello '+this.name
//     }
// }
//
// let earth 	= new Planet("Earth", "Milky Way", 1, 10000);
// let jupiter = new Planet("Jupiter", "Milky Way", 21, 2000000);
//
// // console.log(earth.galaxy)
// console.log(earth.message())