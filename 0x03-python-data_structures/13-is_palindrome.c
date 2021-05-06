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
	int l_length = 0, i = 0, j = 0;
	int a[1000], b[1000];
	listint_t *temp = *head;

	if (*head == NULL)
		return (1);
	l_length = list_len(*head);

	while (i < l_length)
	{
		a[i] = temp->n;
		temp = temp->next;
		i++;
	}
	i--;
	while (i >= 0)
	{
		b[j] = a[i];
		i--;
		j++;
	}
	i = 0;
	while (i < l_length)
	{
		printf("a[%d) = %d\n", i, a[i]);
		printf("b[%d) = %d\n", i, b[i]);
		if (a[i] != b[i])
			return (0);
		i++;
	}
	return (1);
}
