// function hey_there() {
//   console.log("Hi from typescript")
// }
// var fullName: string = "Trenton Denton";
// let paidAccount: boolean = true;
// const versionNumber: number = 1.3;
// function printName(f: string, l: string) {
//   var greeting: string = "Hi there, ";
//   console.log(greeting + f + " " + l);
// }
// console.log(fullName);
// console.log(paidAccount);
// console.log(versionNumber);
// hey_there();
// printName("Trenton", "Denton");
// var msg: string = "Trenton";
// console.log("A long message to " + msg + " filled with text");
// console.log(`A long message to ${msg} filled with text`);
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
// // Booleans
// let paidAccount: Boolean = false;
// // Numbers
// let age: number = 33;
// var taxRate: number = 7.5;
// // Strings
// var fullName: string = "Trenton Denton";
// // Arrays
// var ages: number[] = [33, 28, 11];
// // Tuples
// let player: [number, string, number, number];
// player = [3, "Corerra", .333, 33];
// // Enum
// enum ApprovalStatus { Approved, Pending, Rejected };
// let job: ApprovalStatus = ApprovalStatus.Pending;
// // Any
// var apiData: any[] = [123, "Trenton", false];
// //Void
// function printout(msg: string): void {
//   console.log(msg);
// }
// // Type Aliases
// type PlayerArray = Array<string>;
// let players: PlayerArray = ["Altuve", "Correra", "Bregman"];
// console.log(players);
// // Union Types
// type PlayerArray = Array<string | number>;
// let players: PlayerArray = ["Altuve", "Correra", "Bregman"];
// let playerNumbers: PlayerArray = [25, 3, 2]
// console.log(players);
// console.log(playerNumbers);
// var gradeGenerator(grade: number): string => {
//   if (grade < 60) {
//     return 'F';
//   }
//   if (grade >= 60 && grade < 70) {
//     return 'D';
//   }
//   if (grade >= 70 && grade < 80) {
//     return 'C';
//   }
//   if (grade >= 80 && grade < 90) {
//     return 'B';
//   }
//   if (grade >= 90) {
//     return 'A';
//   }
// }
// gradeGenerator(75);
// var names: string[] = ['Trenton', 'Koda', 'Kaldr'];
// var counter: number = 0;
// (function () {
//   for (let name in names) {
//     counter++;
//   }
// })();
// console.log(counter);
// var fullName: (first: string, last: string) => string;
// fullName = function (first: string, last: string) {
//   return first + " " + last;
// }
// console.log(fullName('Trenton', 'Denton'));
// (function (first: string, last: string) {
//   console.log(first + " " + last);
// })('Kaldr', 'Denton');
//Variables have access to any public variables in the outer scope
// function nameFunction(name: string): void {
//   var n: string = name;
//   function printName() {
//     console.log(n);
//   }
//   printName();
// }
// nameFunction('Trenton');
// function lineup() {
//   var nowBatting: number = 1;
//   return {
//     nextBatter() { nowBatting++ },
//     currentBatter() { return nowBatting }
//   }
// }
// let batters = lineup();
// console.log(batters.currentBatter());
// batters.nextBatter();
// console.log(batters.currentBatter());
// batters.nextBatter();
// console.log(batters.currentBatter());
// interface User {
//   email: string;
//   firstName?: string;
//   lastName?: string;
// }
// class Admin {
//   role: string;
//   constructor(public email: string) {
//     this.role = 'Admin';
//   }
// }
// function profile(user: User): string {
//   return `Welcome, ${user.email}`;
// }
// var joe = new Admin('joe@example.com');
// console.log(joe.role);
// interface IPost {
//   title: string;
//   body: string;
// }
// class Post implements IPost {
//   title: string;
//   body: string;
//   constructor(post: IPost) {
//     this.title = post.title;
//     this.body = post.body;
//   }
//   printPost() {
//     console.log(this.title);
//     console.log(this.body);
//   }
// }
// var post = new Post({ title: "My Great Title", body: "Some content" });
// console.log(post.title);
// console.log(post.body);
// post.printPost();
// namespace Post {
//   export interface IPost {
//     title: string;
//     body: string;
//     slug: string;
//     seoKeywords: string;
//   }
//   export class Post implements IPost {
//     title: string;
//     body: string;
//     slug: string;
//     seoKeywords: string
//     constructor(post: IPost) {
//       this.title = post.title;
//       this.body = post.body;
//       this.slug = post.slug;
//       this.seoKeywords = post.seoKeywords;
//     }
//     printPost() {
//       console.log(this.title);
//       console.log(this.body);
//       console.log(this.slug);
//       console.log(this.seoKeywords);
//     }
//   }
// }
// var blogPost = new Post.Post({
//   title: "My great post",
//   body: "some content",
//   slug: "my-great-post",
//   seoKeywords: "any, words"
// });
// blogPost.printPost();
// interface User { email: string; firstName?: string; lastName?: string; } function profile(user: User): string { return `Welcome, {user.email}`; }
// var realUser = { email: 'test@test.com', firstName: 'Jordan', lastName: 'Hudgens', sayHi() { return "Hey there!"; } };
// console.log(realUser.email);
// class Invoice { companyProfile: string; constructor(public name: string, public city: string, public state: string) { this.companyProfile = name + ", " + city + ", " + state; } }
// var testInvoice = new Invoice('company name', 'city', 'State');
// console.log(testInvoice.name, testInvoice.city, testInvoice.state)
// class Invoice {
//   total: number;
//   constructor(total: number) {
//     this.total = total;
//   }
//   printTotal() {
//     console.log(this.total);
//   }
//   printLater(time: number) {
//     setTimeout(() => {
//       console.log(this.total);
//     }, time)
//   }
// }
// var invoice = new Invoice(400);
// invoice.printTotal();
// invoice.printLater(1000);
// //Higher Order Functions & Callbacks in TypeScript
// var dbQuery = function (): void {
//   setTimeout(() => {
//     console.log('Query Results');
//   }, 3000);
// }
// function loadPage(q: () => void) {
//   console.log("Header");
//   q();
//   console.log("Sidebar");
//   console.log("Footer");
// }
// loadPage(dbQuery);
// "use strict";
// let performUpload = function (imgStatus: string): Promise<{ imgStatus: string }> {
//   return new Promise((resolve) => {
//     console.log(`Status: ${imgStatus}`);
//     setTimeout(() => {
//       resolve({ imgStatus: imgStatus })
//     }, 1000);
//   });
// }
// var upload;
// var compress;
// var transfer;
// performUpload('upload')
//   .then((res) => {
//     upload = res;
//     return performUpload('compressing');
//   })
//   .then((res) => {
//     compress = res;
//     return performUpload('transferring');
//   })
//   .then((res) => {
//     transfer = res;
//     return performUpload('upload completed');
//   });
var AccountsPayable = /** @class */ (function () {
    function AccountsPayable() {
    }
    AccountsPayable.prototype.deleteAccount = function () {
        console.log('Deleting Account');
    };
    __decorate([
        admin
    ], AccountsPayable.prototype, "deleteAccount");
    AccountsPayable = __decorate([
        detailedLog('billing')
    ], AccountsPayable);
    return AccountsPayable;
}());
function detailedLog(dashboard) {
    if (dashboard == 'billing') {
        console.log('Working with the billing department');
        return function (tatget) { };
    }
    else {
        return function (target) { };
    }
}
function admin(target, propertyKey, descriptor) {
    console.log("Doing admin check");
    return descriptor;
}
var post = new AccountsPayable;
post.deleteAccount();
