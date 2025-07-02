import sys
import configparser

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        print(f"✓ Inserted {data} at beginning")
    
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            print(f"✓ Inserted {data} as first element")
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        print(f"✓ Inserted {data} at end")
    
    def delete_node(self, data):
        if not self.head:
            print(f"✗ List is empty, cannot delete {data}")
            return
        
        if self.head.data == data:
            self.head = self.head.next
            print(f"✓ Deleted {data} from beginning")
            return
        
        current = self.head
        while current.next and current.next.data != data:
            current = current.next
        
        if current.next:
            current.next = current.next.next
            print(f"✓ Deleted {data}")
        else:
            print(f"✗ {data} not found in list")
    
    def search(self, data):
        current = self.head
        position = 0
        
        while current:
            if current.data == data:
                print(f"✓ Found {data} at position {position}")
                return position
            current = current.next
            position += 1
        
        print(f"✗ {data} not found in list")
        return -1
    
    def display(self):
        if not self.head:
            print("List: Empty")
            return
        
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        
        print(f"List: {' -> '.join(elements)} -> NULL")
    
    def get_length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

def main():
    if len(sys.argv) != 2:
        print("Usage: python linked_list_ini.py <config_file.ini>")
        sys.exit(1)
    
    config = configparser.ConfigParser()
    config.read(sys.argv[1])
    
    ll = LinkedList()
    
    print("LINKED LIST OPERATIONS")
    print("=" * 30)
    
    # Process operations based on config sections
    for section in config.sections():
        print(f"\n--- {section} ---")
        
        if section == 'INSERT_BEGINNING':
            for key, value in config[section].items():
                ll.insert_at_beginning(int(value))
        
        elif section == 'INSERT_END':
            for key, value in config[section].items():
                ll.insert_at_end(int(value))
        
        elif section == 'DELETE':
            for key, value in config[section].items():
                ll.delete_node(int(value))
        
        elif section == 'SEARCH':
            for key, value in config[section].items():
                ll.search(int(value))
        
        elif section.startswith('DISPLAY'):
            ll.display()
            print(f"Length: {ll.get_length()}")

if __name__ == "__main__":
    main()
