#include "hash_tables.h"

unsigned long int key_index(const unsigned char *key, unsigned long int size)
{
	unsigned long int key2;

	key2 = hash_djb2(key);
	return key2 % size;

}
