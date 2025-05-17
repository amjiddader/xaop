import os
import random
import string
from datetime import datetime

# Dictionary of programming languages with their file extensions and some common keywords/syntax
LANGUAGES = {
    'python': {'ext': 'py', 'keywords': ['def', 'class', 'import', 'from', 'if', 'for', 'while', 'try', 'except', 'return']},
    'javascript': {'ext': 'js', 'keywords': ['function', 'const', 'let', 'var', 'if', 'for', 'while', 'try', 'catch', 'return']},
    'java': {'ext': 'java', 'keywords': ['public', 'class', 'private', 'void', 'static', 'if', 'for', 'while', 'try', 'catch']},
    'cpp': {'ext': 'cpp', 'keywords': ['int', 'void', 'class', 'public', 'private', 'if', 'for', 'while', 'try', 'catch']},
    'rust': {'ext': 'rs', 'keywords': ['fn', 'struct', 'impl', 'let', 'mut', 'if', 'for', 'while', 'match', 'return']},
    'go': {'ext': 'go', 'keywords': ['func', 'type', 'struct', 'var', 'if', 'for', 'range', 'defer', 'return']},
    'ruby': {'ext': 'rb', 'keywords': ['def', 'class', 'module', 'if', 'unless', 'while', 'begin', 'rescue', 'end']},
    'php': {'ext': 'php', 'keywords': ['function', 'class', 'public', 'private', 'if', 'foreach', 'while', 'try', 'catch']},
    'swift': {'ext': 'swift', 'keywords': ['func', 'class', 'struct', 'var', 'let', 'if', 'for', 'while', 'try', 'guard']},
    'kotlin': {'ext': 'kt', 'keywords': ['fun', 'class', 'val', 'var', 'if', 'for', 'while', 'try', 'catch']},
    'typescript': {'ext': 'ts', 'keywords': ['interface', 'type', 'class', 'const', 'let', 'if', 'for', 'while', 'try', 'catch']},
    'csharp': {'ext': 'cs', 'keywords': ['public', 'class', 'private', 'void', 'static', 'if', 'for', 'while', 'try', 'catch']},
    'scala': {'ext': 'scala', 'keywords': ['def', 'class', 'object', 'val', 'var', 'if', 'for', 'while', 'try', 'catch']},
    'r': {'ext': 'r', 'keywords': ['function', 'if', 'for', 'while', 'repeat', 'break', 'next', 'return']},
    'perl': {'ext': 'pl', 'keywords': ['sub', 'package', 'my', 'if', 'unless', 'while', 'for', 'foreach']},
    'shell': {'ext': 'sh', 'keywords': ['if', 'then', 'else', 'fi', 'while', 'do', 'done', 'case', 'esac']},
    'sql': {'ext': 'sql', 'keywords': ['SELECT', 'FROM', 'WHERE', 'JOIN', 'GROUP BY', 'ORDER BY', 'INSERT', 'UPDATE']},
    'lua': {'ext': 'lua', 'keywords': ['function', 'local', 'if', 'then', 'else', 'for', 'while', 'repeat']},
    'dart': {'ext': 'dart', 'keywords': ['class', 'void', 'var', 'final', 'if', 'for', 'while', 'try', 'catch']},
    'julia': {'ext': 'jl', 'keywords': ['function', 'struct', 'module', 'if', 'for', 'while', 'try', 'catch']},
    'haskell': {'ext': 'hs', 'keywords': ['data', 'type', 'class', 'instance', 'where', 'let', 'in', 'case', 'of']},
    'erlang': {'ext': 'erl', 'keywords': ['-module', 'export', 'if', 'case', 'of', 'receive', 'after']},
    'elixir': {'ext': 'ex', 'keywords': ['def', 'defmodule', 'if', 'do', 'case', 'cond', 'rescue']},
    'matlab': {'ext': 'm', 'keywords': ['function', 'if', 'else', 'for', 'while', 'try', 'catch']},
    'groovy': {'ext': 'groovy', 'keywords': ['def', 'class', 'if', 'for', 'while', 'try', 'catch']},
    'vb': {'ext': 'vb', 'keywords': ['Public', 'Private', 'Function', 'Sub', 'If', 'For', 'While', 'Try']},
    'cobol': {'ext': 'cob', 'keywords': ['PROGRAM-ID', 'PROCEDURE', 'PERFORM', 'IF', 'ELSE', 'END-IF']},
    'pascal': {'ext': 'pas', 'keywords': ['program', 'procedure', 'function', 'begin', 'end', 'if', 'for', 'while']},
    'fortran': {'ext': 'f90', 'keywords': ['program', 'subroutine', 'function', 'if', 'do', 'end']},
    'assembly': {'ext': 'asm', 'keywords': ['section', 'global', 'mov', 'push', 'pop', 'call', 'ret']},
}

def generate_fake_code(language, keywords):
    """Generate fake but realistic-looking code for a given language."""
    lines = []
    name_chars = string.ascii_letters + string.digits + '_'
    
    # Add some comments
    comments = {
        'py': '#', 'js': '//', 'java': '//', 'cpp': '//', 'rs': '//', 'go': '//',
        'rb': '#', 'php': '//', 'swift': '//', 'kt': '//', 'ts': '//', 'cs': '//',
        'scala': '//', 'r': '#', 'pl': '#', 'sh': '#', 'sql': '--', 'lua': '--',
        'dart': '//', 'jl': '#', 'hs': '--', 'erl': '%', 'ex': '#', 'm': '%',
        'groovy': '//', 'vb': "'", 'cob': '*>', 'pas': '//', 'f90': '!', 'asm': ';'
    }
    
    comment_char = comments.get(language['ext'], '//')
    lines.append(f"{comment_char} Generated code for {language['ext']} file")
    lines.append(f"{comment_char} Created on: {datetime.now()}")
    lines.append("")
    
    # Generate multiple code blocks
    for _ in range(random.randint(3, 7)):
        # Generate random identifiers
        identifiers = [''.join(random.choices(name_chars, k=random.randint(4, 12))) for _ in range(5)]
        
        # Mix keywords and identifiers to create fake code
        for _ in range(random.randint(10, 20)):
            line_parts = []
            line_parts.extend(random.choices(keywords, k=random.randint(1, 3)))
            line_parts.extend(random.choices(identifiers, k=random.randint(1, 2)))
            line = ' '.join(line_parts)
            
            # Add some common punctuation
            if random.random() < 0.3:
                line += ';'
            elif random.random() < 0.2:
                line += ' {'
            elif random.random() < 0.2:
                line += ' }'
                
            lines.append(line)
        lines.append("")
    
    return '\n'.join(lines)

def delete_files(data_folder):
    print("Starting to delete all files in data folder...")
    for filename in os.listdir(data_folder):
        file_path = os.path.join(data_folder, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)
            print(f"Deleted {file_path}")
    
    # Sleep for 3 seconds after all deletions
    print("Sleeping for 3 seconds before generating new files...")
    from time import sleep
    sleep(3)

def create_language_files(data_folder, max_size_mb=3):
    print(f"\nGenerating {len(LANGUAGES)} language files...")
    for lang_name, lang_info in LANGUAGES.items():
        file_path = os.path.join(data_folder, f"code.{lang_info['ext']}")
        fake_code = generate_fake_code(lang_info, lang_info['keywords'])
        
        # Ensure the file size is approximately what we want by repeating the content
        while len(fake_code.encode('utf-8')) < max_size_mb * 124 * 124:
            fake_code += "\n" + generate_fake_code(lang_info, lang_info['keywords'])
        
        # Write the file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(fake_code)
        print(f"Generated {file_path} ({len(fake_code.encode('utf-8')) / (124*124):.2f} MB)")

data_folder = 'data'
if not os.path.exists(data_folder):
    os.makedirs(data_folder)

if __name__ == "__main__":
    delete_files(data_folder)
    create_language_files(data_folder)
 