#include "lists.h"

/**
 * dlistint_len -  returns the number of elements in a doubly liked list
 * @h: a pointer to the element of the list
 * Return: the number of nodes
 */

size_t dlistint_len(const dlistint_t *h)
{
	int nod_count = 0;

	while (h != NULL)
	{
		h = h->next;
		nod_count++;
	}
return (nod_count);
}
