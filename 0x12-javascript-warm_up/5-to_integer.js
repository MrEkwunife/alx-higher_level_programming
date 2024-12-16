#!/usr/bin/node
const arg = process.argv[2]
const val = parseInt(arg) ? `My number: ${parseInt(arg)}` : 'Not a number';
console.log(val);
