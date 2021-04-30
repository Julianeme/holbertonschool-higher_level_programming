#include "lists.h"
#include <stdio.h>

/**
 * get_dnodeint_at_index - returns the data of the nth node of
 * a doubly linked list
 * @head: a double pointer to the head of the linked list
 * @index: requested node
 * Return: the requested node's data
 */

dlistint_t *get_dnodeint_at_index(dlistint_t *head, unsigned int index)
{
	unsigned int i = 0;
	dlistint_t *temp = NULL;

	if (head == NULL)
		return (NULL);
	temp = head;
	while (i < index)
	{
		if (temp->next == NULL && i !=  index - 1)
		{
			return (NULL);
		}
		temp = temp->next;
		i++;
	}
	return (temp);
}
