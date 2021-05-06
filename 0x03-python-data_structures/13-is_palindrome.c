#include <stdio.h>
#include <limits.h>
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
	int l_length = 0, i = 0, j;
	listint_t *temp = *head;
	int array[BUFSIZ];

	if (*head == NULL)
		return (1);
	l_length = list_len(*head);
	j = l_length;
	while (i < j)
	{
		array[i] = temp->n;
		temp = temp->next;
		i++;
	}
	temp = *head;
	i = 0;
	while (i < l_length / 2)
	{
		printf("array[%d] =  %d   ---  temp->next = %d\n", i, array[i], temp->n);
		if (temp->n != array[j - 1])
		{
			printf("array[%d] =  %d   ---  temp->next = %d\n", i, array[i], temp->n);
			return (0);
		}
		temp = temp->next;
		j--;
		i++;
	}
	return (1);
}
