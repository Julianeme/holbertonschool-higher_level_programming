#include <stdio.h>
#include "lists.h"

/**
* list_len - returns the number of nodes in a liked list
* @h: a pointer to the element of the list
* Return: the number of nodes
*/

size_t list_len(const listint_t *h)
{
	int nod_count = 0;

	while (h != NULL)
	{
		h = h->next;
		nod_count++;
	}
	return (nod_count);
}

/**
 * is_palindrome - checks if a linked list is palindrome
 * @head: a double pointer to the first element of the list
 * Return: 1 if palindrome, 0 if not
 */

int is_palindrome(listint_t **head)
{
	int l_length = 0, i = 0, j = 0, l = 0;
	listint_t *temp = *head, *aux = *head;

	if (*head == NULL)
		return (1);
	l_length = list_len(*head);
	j = l_length;
	l = j;
	i = 0;
	j = 1;
	while (i < l_length / 2)
	{
		temp = *head;
		while (j < l)
		{
			temp = temp->next;
			j++;
		}
		j = 1;
		l = l - 1;
		if (aux->n != temp->n)
			return (0);
		aux = aux->next;
		i++;
	}
	return (1);
}
