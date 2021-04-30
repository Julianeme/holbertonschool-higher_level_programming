#include "lists.h"
#include <stdio.h>

/**
 * delete_dnodeint_at_index - deletes a node at the given position
 * in a doubly linked list
 * @head: a double pointer to the head of the linked list
 * @index: the position of the node to be deleted
 * Return: 1 on success, -1 otherwise
 */

int delete_dnodeint_at_index(dlistint_t **head, unsigned int index)
{
	unsigned int i = 0;
	dlistint_t *temp = *head;

	if (!*head)
		return (-1);
	if (index == 0)
	{
		if (temp->next)
		{
			*head = temp->next;
			temp->next->prev = NULL;
		}
		else
		{
			*head = NULL;
			return (1);
		}
	}
	else
	{
		while (i < index)
		{
			i++;
			if ((temp->next == NULL) && (i != (index - 2)))
				return (-1);
			temp = temp->next;
		}
		temp->prev->next = temp->next;
		temp->next->prev =  temp->prev;
	}
	free(temp);
	return (1);
}
