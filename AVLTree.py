#id1: 209858182
#name1: rebecca edelstein
#username1:
#id2:
#name2:
#username2:


"""A class represnting a node in an AVL tree"""

class AVLNode(object):
	"""Constructor, you are allowed to add more fields. 
	
	@type key: int
	@param key: key of your node
	@type value: string
	@param value: data of your node
	"""
	def __init__(self, key, value):
		self.key = key
		self.value = value
		self.left = None
		self.right = None
		self.parent = None
		self.height = -1
		

	"""returns whether self is not a virtual node 

	@rtype: bool
	@returns: False if self is a virtual node, True otherwise.
	"""
	def is_real_node(self):
		if self.key == None:
			return False
		return True

	"""returns whether self is right child 
		@rtype: bool
		@returns: False if self is a left child, True otherwise.
		complexity: O(1)
		"""

	def is_right_child(self):
		if self.parent == None:
			return False
		if (self.parent.left == self):
			return False
		return True

	"""returns the key
    Complexity: O(1)
    @rtype: int or None
    @returns: the key of self, None if the node is virtual
    """


	def get_key(self):
		return self.key

	"""switch between two AVL nodes by replacing their pointers
		@rtype: void
		@param other: AVLNode
		complexity: O(1)
		"""

	def replace(self, other):
		self_height = self.get_height()
		self.set_height(other.get_height())
		other.set_height(self_height)
		other.set_parent(self.parent)
		other.set_right(self.right)
		other.set_left(self.left)
		self.right.set_parent(other)
		self.left.set_parent(other)
		if self.is_right_child():
			self.parent.set_right(other)
		else:
			if self.parent != None:
				self.parent.set_left(other)

	"""returns the value
    Complexity: O(1)
    @rtype: any
    @returns: the value of self, None if the node is virtual
    """

	def get_value(self):
		return self.value

	"""returns the left child
    Complexity: O(1)
    @rtype: AVLNode
    @returns: the left child of self, None if there is no left child (if self is virtual)
    """

	def get_left(self):
		if not self.is_real_node():
			return None
		return self.left

	"""returns the right child
    Complexity: O(1)
    @rtype: AVLNode
    @returns: the right child of self, None if there is no right child (if self is virtual)
    """

	def get_right(self):
		if not self.is_real_node():
			return None
		return self.right

	"""returns the parent 
    Complexity: O(1)
    @rtype: AVLNode
    @returns: the parent of self, None if there is no parent
    """

	def get_parent(self):
		return self.parent

	"""returns the height
    Complexity: O(1)
    @rtype: int
    @returns: the height of self, -1 if the node is virtual
    """

	def get_height(self):
		return self.height

	"""sets key
    Complexity: O(1)
    @type key: int or None
    @param key: key
    """

	def set_key(self, key):
		self.key = key

	"""returns the value
    Complexity: O(1)
    @rtype: any
    @returns: the value of self, None if the node is virtual
    """

	def set_value(self, value):
		self.value = value

	"""sets left child
    Complexity: O(1)
    @type node: AVLNode
    @param node: a node
    """

	def set_left(self, left):
		self.left = left

	"""sets right child
    Complexity: O(1)
    @type node: AVLNode
    @param node: a node
    """

	def set_right(self, right):
		self.right = right

	"""sets parent
    Complexity: O(1)
    @type node: AVLNode
    @param node: a node
    """

	def set_parent(self, parent):
		self.parent = parent

	"""sets the height of the node
    Complexity: O(1)
    @type h: int
    @param h: the height
    """

	def set_height(self, height):
		self.height = height


	"""calculates height
		@rtype: int
		@returns: max between height of left child and height of right child + 1
		complexity: O(1)
		"""

	def check_height(self):
		left_height = self.get_left().get_height() if self.get_left() else -1  # If left is None, height is -1
		right_height = self.get_right().get_height() if self.get_right() else -1  # If right is None, height is -1
		return max(left_height, right_height) + 1

	"""calculates the balance factor of a given node

    @type node: AVLNode
    @rtype: int
	@return: the balance factor of the current node
    """

	def get_BF(self):
		return (self.left.height if self.left else 0) - (self.right.height if self.right else 0)


"""
A class implementing an AVL tree.
"""

class AVLTree(object):

	"""
	Constructor, you are allowed to add more fields.
	"""
	def __init__(self):
		self.root = None


	"""searches for a node in the dictionary corresponding to the key (starting at the root)
        
	@type key: int
	@param key: a key to be searched
	@rtype: (AVLNode,int)
	@returns: a tuple (x,e) where x is the node corresponding to key (or None if not found),
	and e is the number of edges on the path between the starting node and ending node+1.
	"""


	def search(self, key):
		path_len = 0
		if key == None or self.root == None:
			return None, path_len
		# Start search at the root
		curr_node = self.root
		while curr_node.is_real_node():
			path_len += 1
			if key == curr_node.get_key():
				return curr_node, path_len

			if key < curr_node.get_key():
				curr_node = curr_node.get_left()  # Key is less than current key - search in left sub-tree
			else:
				curr_node = curr_node.get_right()  # Key is greater than current key - search in right sub-tree
		return None, path_len


	"""searches for a node in the dictionary corresponding to the key, starting at the max
        
	@type key: int
	@param key: a key to be searched
	@rtype: (AVLNode,int)
	@returns: a tuple (x,e) where x is the node corresponding to key (or None if not found),
	and e is the number of edges on the path between the starting node and ending node+1.
	"""

	def finger_search(self, key):

		path_len = 0
		curr_node = self.max_node()

		# the key is invalid or the tree is empty
		if key == None or curr_node == None:
			return None, path_len

		#Traverse from the max to the node which is the root of the subtree that contains the key (if root is not max)
		while (curr_node.is_real_node()
			   and curr_node.get_parent() is not None
			   and curr_node.get_parent().is_real_node()
			   and curr_node.get_parent().get_key() >= key):

			path_len += 1
			if key == curr_node.get_key():
				return curr_node, path_len
			else:
				curr_node = curr_node.get_parent()

		#we are at the root of the subtree, now go one left (only if there is also a right, cause we already visited the right)
		if curr_node.get_left().is_real_node() and curr_node.get_right().is_real_node():
			if curr_node.get_key() == key:
				path_len += 1
				return curr_node, path_len
			curr_node = curr_node.get_left()
			path_len += 1

		#search for the key in the subtree
		while curr_node.is_real_node():
			path_len += 1
			if key == curr_node.get_key():
				return curr_node, path_len

			if key < curr_node.get_key():
				curr_node = curr_node.get_left()
			else:
				curr_node = curr_node.get_right()

		return None, path_len

	"""performs a left rotation and updates fields accordingly

	    @type node: AVLNode
	    @param node: the node we're performing the rotation on
	    @pre: node is in self, has a right son, and its right son has a left son
	    """

	'''def left_rotate(self, node):
		new_root = node.right
		left_subtree = new_root.left
		new_root.left = node
		node.right = left_subtree
		if left_subtree is not None:
			left_subtree.parent = node
		new_root.parent = node.parent
		node.parent = new_root
		node.height = 1 + max(node.left.height if node.left else 0, node.right.height if node.right else 0)
		new_root.height = 1 + max(new_root.left.height if new_root.left else 0,
								  new_root.right.height if new_root.right else 0)
		if new_root.parent is None:
			self.root = new_root
		return new_root

	"""performs a right rotation and updates fields accordingly

    @type node: AVLNode
    @param node: the node we're performing the rotation on
    @pre: node is in self, has a left son, and its left son has a right son
    """

	def right_rotate(self, node):
		new_root = node.left
		right_subtree = new_root.right
		new_root.right = node
		node.left = right_subtree
		if right_subtree is not None:
			right_subtree.parent = node
		new_root.parent = node.parent
		node.parent = new_root
		node.height = 1 + max(node.left.height if node.left else 0, node.right.height if node.right else 0)
		new_root.height = 1 + max(new_root.left.height if new_root.left else 0,
								  new_root.right.height if new_root.right else 0)
		if new_root.parent is None:
			self.root = new_root
		return new_root'''

	"""doing right rotaion in order to keep the tree balace
	@type criminal: AVLNode
	@param criminal: the node with the balance factor 2 
	complexity: O(1)
	"""
	def RightRotation(self, criminal):
		criminal_left = criminal.get_left()
		criminal_is_right_child = criminal.is_right_child()
		criminal.set_left(criminal_left.get_right())
		criminal.get_left().set_parent(criminal)
		criminal_left.set_right(criminal)
		criminal_left.set_parent(criminal.get_parent())
		if criminal_is_right_child:
			criminal_left.get_parent().set_right(criminal_left)
		else:
			if self.root == criminal:
				self.root = criminal_left
			else:
				criminal_left.get_parent().set_left(criminal_left)
		criminal.set_parent(criminal_left)
		criminal.set_height(criminal.check_height())
		criminal_left.set_height(criminal_left.check_height())


	"""doing left rotaion in order to keep the tree balace
	@type criminal: AVLNode
	@param criminal: the node with the balance factor -2
	complexity: O(1)
	"""
	def LeftRotation(self, criminal):
		criminal_right = criminal.get_right()
		criminal_is_right_child = criminal.is_right_child()
		criminal.set_right(criminal_right.get_left())
		criminal.get_right().set_parent(criminal)
		criminal_right.set_left(criminal)
		criminal_right.set_parent(criminal.get_parent())
		if criminal_is_right_child:
			criminal_right.get_parent().set_right(criminal_right)
		else:
			if self.root == criminal:
				self.root = criminal_right
			else:
				criminal_right.get_parent().set_left(criminal_right)
		criminal.set_parent(criminal_right)
		criminal.set_height(criminal.check_height())
		criminal_right.set_height(criminal_right.check_height())

	"""balances input AVLTree using rotations

    @type node: AVLNode 
    @param node: a node to perform balancing from
    @pre: node is in self
    """
	def balance(self, case , node_to_insert_parent):
		num_promotions = 0
		#The loop ensures we check each node on the path to the root for balance violations
		while node_to_insert_parent!= None: #going all the way to the root
			grandpa = node_to_insert_parent.get_parent()
			bf = node_to_insert_parent.get_BF()
			new_height = node_to_insert_parent.check_height()

			if abs(bf) < 2: # Current balance factor is good
				if new_height != node_to_insert_parent.get_height():
					node_to_insert_parent.set_height(new_height)
					num_promotions += 1
				node_to_insert_parent = grandpa
			else:
				if bf == -2:
					right_bf = node_to_insert_parent.get_right().get_BF()
					if  right_bf== -1 or (right_bf == 0 and case == "delete"):
						self.LeftRotation(node_to_insert_parent)
					else:
						self.RightRotation(node_to_insert_parent.get_right())
						self.LeftRotation(node_to_insert_parent)
				else:
					left_bf = node_to_insert_parent.get_left().get_BF()
					if left_bf == 1 or (left_bf == 0 and case == "delete"):
						self.RightRotation(node_to_insert_parent)
					else:
						self.LeftRotation(node_to_insert_parent.get_left())
						self.RightRotation(node_to_insert_parent)

				node_to_insert_parent = grandpa

		return num_promotions

	"""insert node in a binary search tree
	@type node: AVLNode
	@param node: node to insert
	complexity: O(log n)
	"""

	def insertBST(self, node):
		curr = self.root
		path_len = 0
		curr_parent = None
		# if the tree is empty, the node is inserted at the root
		if curr == None:
			self.root = node
		# if the tree is not empty
		else:
			#we traverse the tree until we get to a NONE node
			while curr.is_real_node():
				curr_parent = curr
				path_len += 1
				if node.key < curr.get_key():
					curr = curr.get_left()
				else:
					curr = curr.get_right()
			#we found the parent to which we will attach the new node
			if node.key < curr_parent.get_key():
				curr_parent.set_left(node)
			else:
				curr_parent.set_right(node)

			node.set_parent(curr_parent) #set the parent of this node to be the curr_parent
		node.set_height(node.check_height())
		return node, path_len

	''''inserts a new node into the dictionary with corresponding key and value (starting at the root)
	@type key: int
	@pre: key currently does not appear in the dictionary
	@param key: key of item that is to be inserted to self
	@type val: string
	@param val: the value of the item
	@rtype: (AVLNode,int,int)
	@returns: a 3-tuple (x,e,h) where x is the new node,
	e is the number of edges on the path between the starting node and new node before rebalancing,
	and h is the number of PROMOTE cases during the AVL rebalancing'''

	def insert(self, key, val):

		num_promotions = 0

		node_to_insert = AVLNode(key, val)
		node_to_insert.set_left(AVLNode(None, None))
		node_to_insert.set_right(AVLNode(None, None))
		node_to_insert.get_left().set_parent(node_to_insert)
		node_to_insert.get_right().set_parent(node_to_insert)
		inserted_node, path_len = self.insertBST(node_to_insert)
		#we inserted the node, now we need to rebalance.
		if not self.get_root().get_right().is_real_node() and not self.get_root().get_left().is_real_node():
			return inserted_node, path_len, 0 #the tree contains only the node, no need to rebalance

		else: # we need to rebalance
			num_promotions = self.balance("insert",node_to_insert.get_parent())
			return inserted_node, path_len, num_promotions

	"""searches for the parent of a node in the dictionary corresponding to the key, starting at the max

		@type key: int
		@param key: a key to be searched
		@rtype: (AVLNode,int)
		@returns:  (y,e) where y is the parent of node corresponding to key (or None if not found),
		and e is the number of edges on the path between the starting node and ending node+1.
		"""

	def finger_search_parent(self, key):

		path_len = 0
		curr_node = self.max_node()
		# the key is invalid or the tree is empty
		if key == None or curr_node == None:
			return None, path_len

		# traverse from the max to the node which is the root of the subtree that contains the key (if root is not max)
		while (curr_node.is_real_node()
			   and curr_node.get_parent() is not None
			   and curr_node.get_parent().is_real_node()
			   and curr_node.get_parent().get_key() >= key):

			path_len += 1
			if key == curr_node.get_key():
				return curr_node, path_len
			else:
				curr_node = curr_node.get_parent()

		# we are at the root of the subtree, now go one left (only if there is also a right, cause we already visited the right)
		if curr_node.get_left().is_real_node() and curr_node.get_right().is_real_node():
			parent = curr_node
			curr_node = curr_node.get_left()
			path_len += 1

		# search for the key in the subtree
		while curr_node.is_real_node():
			path_len += 1
			if key == curr_node.get_key():
				return curr_node, path_len

			if key < curr_node.get_key():
				parent = curr_node
				curr_node = curr_node.get_left()
			else:
				parent = curr_node
				curr_node = curr_node.get_right()

		return parent, path_len

	"""insert node in a binary search tree, starting at the max
		@type node: AVLNode
		@param node: node to insert
		"""

	def finger_insertBST(self, node):
		curr = self.max_node()
		path_len = 0
		# if the tree is empty, the node is inserted at the root
		if  curr == None:
			self.root = node
		# if the tree is not empty
		else:
			#we do a finger_search() to find the spot of insertion
			parent, path_len = self.finger_search_parent(node.key)

			# we found the parent to which we will attach the new node
			if node.key < parent.get_key():
				parent.set_left(node)
			else:
				parent.set_right(node)

			node.set_parent(parent)  # set the parent of this node to be the last_parent
		node.set_height(node.check_height())
		return node, path_len


	"""inserts a new node into the dictionary with corresponding key and value, starting at the max

	@type key: int
	@pre: key currently does not appear in the dictionary
	@param key: key of item that is to be inserted to self
	@type val: string
	@param val: the value of the item
	@rtype: (AVLNode,int,int)
	@returns: a 3-tuple (x,e,h) where x is the new node,
	e is the number of edges on the path between the starting node and new node before rebalancing,
	and h is the number of PROMOTE cases during the AVL rebalancing
	"""
	def finger_insert(self, key, val):

		num_promotions = 0
		node_to_insert = AVLNode(key, val)
		node_to_insert.set_left(AVLNode(None, None))
		node_to_insert.set_right(AVLNode(None, None))
		node_to_insert.get_left().set_parent(node_to_insert)
		node_to_insert.get_right().set_parent(node_to_insert)
		inserted_node, path_len = self.finger_insertBST(node_to_insert)
		# we inserted the node, now we need to rebalance.
		if not self.get_root().get_right().is_real_node() and not self.get_root().get_left().is_real_node():
			return inserted_node, path_len, 0  # the tree contains only the node, no need to rebalance

		else:  # we need to rebalance
			num_promotions = self.balance("insert", node_to_insert.get_parent())
			return inserted_node, path_len, num_promotions

	"""searches for the node with the min key bigger then self 
		@type node: AVLNode
		@param key: a node successor to be searched
		@rtype: AVLNode
		@returns: successor node 
		compleity: worst case is O(log n)
		"""

	def successor(self, node):
		if not node or not node.is_real_node():
			return None
		curr = node
		if curr.get_right().is_real_node():
			curr = curr.get_right()
			while curr.get_left().is_real_node():
				curr = curr.get_left()
			return curr
		parent = curr.get_parent()
		while parent != None and parent.is_real_node() and curr.is_right_child():
			curr = parent
			parent = curr.get_parent()
		return parent  # If node has the maximum key, None will be returned

	"""delete binary search tree
		@type node: AVLNode
		@param node: node to delete
		complexity: O(log n) ,(because of successor)
		"""

	def deleteBST(self, node):
		right_child = node.get_right()
		left_child = node.get_left()
		has_right = right_child.is_real_node()
		has_left = left_child.is_real_node()
		parent = node.get_parent()
		# Case 1: Node is a leaf
		if not has_left and not has_right:
			if parent == None:
				self.root = None
			elif node.is_right_child():
				parent.set_right(AVLNode(None, None))
				parent.get_right().set_parent(parent)
			else:
				parent.set_left(AVLNode(None, None))
				parent.get_left().set_parent(parent)
		# Case 2: Node has two children
		elif has_right and has_left:
			follower = self.successor(node)
			# Remove successor from tree
			if follower.is_right_child():
				follower.get_parent().set_right(follower.get_right())
			else:
				follower.get_parent().set_left(follower.get_right())
			follower.get_right().set_parent(follower.get_parent())
			# Replace node with its successor
			node.replace(follower)
			if self.root == node:
				self.root = follower
		# Case 3 (and last): Node has one child
		else:
			if has_right:
				child = right_child
			else:
				child = left_child
			if parent == None:
				self.root = child
			elif node.is_right_child():
				parent.set_right(child)
			else:
				parent.set_left(child)
			child.set_parent(parent)

	"""deletes node from the dictionary

	@type node: AVLNode
	@pre: node is a real pointer to a node in self
	"""
	def delete(self, node):
		# Save parent of deleted node, for rebalancing
		follower = self.successor(node)
		if node.get_right().is_real_node() and node.get_left().is_real_node():
			y = follower.get_parent()
			# In case the successor is the node's right child
			if follower == node.get_right():
				y = follower
		else:
			y = node.get_parent()
		self.deleteBST(node)
		self.balance("delete",y)
		return	

	
	"""joins self with item and another AVLTree

	@type tree2: AVLTree 
	@param tree2: a dictionary to be joined with self
	@type key: int 
	@param key: the key separting self and tree2
	@type val: string
	@param val: the value corresponding to key
	@pre: all keys in self are smaller than key and all keys in tree2 are larger than key,
	or the opposite way
	"""
	def join(self, tree2, key, val):
		return


	"""splits the dictionary at a given node

	@type node: AVLNode
	@pre: node is in self
	@param node: the node in the dictionary to be used for the split
	@rtype: (AVLTree, AVLTree)
	@returns: a tuple (left, right), where left is an AVLTree representing the keys in the 
	dictionary smaller than node.key, and right is an AVLTree representing the keys in the 
	dictionary larger than node.key.
	"""
	def split(self, node):
		return None, None

	
	"""returns an array representing dictionary 

	@rtype: list
	@returns: a sorted list according to key of tuples (key, value) representing the data structure
	"""
	def avl_to_array(self):
		return None


	"""returns the node with the maximal key in the dictionary

	@rtype: AVLNode
	@returns: the maximal node, None if the dictionary is empty
	"""
	def max_node(self):
		if self.root == None:
			return None  # The tree is empty

		current = self.root
		while current.right.is_real_node():  # Traverse to the rightmost node
			current = current.right

		return current

	"""Helper function to calculate the size of the subtree rooted at the given node.

	    @type node: AVLNode
	    @param node: the root of the subtree
	    @rtype: int
	    @return: the size of the subtree
	    """

	def size_helper(self, node):
		if node is None or not node.is_real_node():
			return 0
		leftSubtree = self.size_helper(node.right) if node.right is not None else 0
		rightSubtree = self.size_helper(node.left) if node.left is not None else 0
		return 1 + leftSubtree + rightSubtree;

	"""returns the number of items in dictionary 

    @rtype: int
    @returns: the number of items in dictionary, should only work on trees that were made entirely of insert,delete,join without split
    """

	def size(self):
		if self.root is None:
			return 0
		size = self.size_helper(self.root)
		return size


	"""returns the root of the tree representing the dictionary

	@rtype: AVLNode
	@returns: the root, None if the dictionary is empty
	"""
	def get_root(self):
		return self.root

