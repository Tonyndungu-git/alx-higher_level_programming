#!/usr/bin/node

const arg = process.argv[2];
const parsedNumber = parseInt(arg);

if (!isNaN(parsedNumber))
{
    console.log(`My Number: ${parsedNumber}`)
}
else
{
    console.log('Not a Number')

}
