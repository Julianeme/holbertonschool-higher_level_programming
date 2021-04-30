#include "lists.h"
#include <stdio.h>

/**
 * insert_dnodeint_at_index - inserts a node at the given position
 * in a doubly linked list
 * @h: a double pointer to the head of the linked list
 * @idx: node insertion position
 * @n: the int value stored in the node
 * Return: the address of the temp node
 */

dlistint_t *insert_dnodeint_at_index(dlistint_t **h, unsigned int idx, int n)
{
	unsigned int i = 0;
	dlistint_t *temp = *h, *new = NULL;

	new = malloc(sizeof(dlistint_t));
	if (!new)
		return (NULL);
	new->n = n;
	if (idx == 0)
	{
		new->prev = NULL;
		new->next = *h;
		*h = new;
	}
	else
	{
		while (i < idx)
		{
			i++;
			if ((temp->next == NULL) && (i != (idx - 2)))
				return (NULL);
			temp = temp->next;
			if ((!temp->next) && (i == idx - 1))
			{
				new->next = NULL;
				new->prev = temp;
				temp->next = new;
				return (new);
			}

		}
		new->next = temp;
		new->prev = temp->prev;
		temp->prev = new;
		temp = temp->prev->prev;
		temp->next = new;
	}
	return (new);
}
