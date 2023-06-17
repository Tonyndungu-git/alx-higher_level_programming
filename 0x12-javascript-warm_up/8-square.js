#!/usr/bin/node

const args = process.argv.slice(2);
const a = parseInt(args[0]);

let i = 0;
while (i < a)
{
    let j=0;
    while (j < a -1)
    {
	if (i === 0 || i === a - 1 || j === 0 || j === a - 1)
	{
	    process.stdout.write('x');
	}
	else
	{
	    process.stdout.write(' ');
	}

	j++;
    }
    console.log('x')
    i++;
}
