#include "hash_tables.h"

/**
 * hash_djb2 - djb2 algorithm
 * @str: pointer
 * Return: unsigned long int
 **/


unsigned long int hash_djb2(const unsigned char *str)
{
	unsigned long hash;
	int c;

	hash = 5003;
	while ((c = *str++))
	{
		hash = ((hash << 5) + hash) ^ c;

	}
	return (hash);
}
