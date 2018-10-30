# <table style="width:100%">
#   <tr>
#     <th>Authors</th>
#     <th>Title</th>
#     <th>Year</th>
#     <th>Venue</th>
#     <th>Link(s)</th>
#     <th>Arxiv</th>
#   </tr>
#   <tr>
#     <td>?</td>
#     <td>?</td>
#     <td>?</td>
#     <td>?</td>
#     <td>?</td>
#     <td>?</td>
#   </tr>
#   ...
# </table>

rows = []

def get(text,col):
    columns = {'authors':0,'title':1,'year':3,'venue':2,'links':4,'arxiv':5,'tags':6}
    return text.split('\t')[columns[col]]


def link(line):
    x = get(line,'links')
    if 'href' in x:
        return x
    elif x.strip():
        return f'<a href="{x}">pdf</a>'
    else:
        return ''

def arxiv(line):
    x = get(line,'arxiv')
    if x.strip():
        return f'<a href="{x}">arxiv</a>'
    else:
        return ''

def tags(line):
    tags = []
    x = get(line,'tags')
    x = x.split(', ')
    for tag in x:
        if not tag.strip(): continue
        tag = tag.replace('"','')
        tags.append(f'<button class="{tag}" on="0">{tag}</button>')
    return ' '.join(tags)

file = 'amr_papers.tsv'
file2 = 'amr_papers.html'
template = open('template.html','r',encoding='utf8').read()
with open(file, 'r', encoding='utf8') as f:
    i = 0
    l, r='{','}'
    for line in f:
        if i==0:
            i+=1
            continue
        bib = f'''
            <tr>
                <td>{get(line,'title')} </td>
                <td>({get(line,'authors')})</td>
                <td>{get(line,'venue')}</td>
                <td>{get(line,'year')}</td>
                <td>{link(line)}</td>
                <td>{arxiv(line)}</td>
                <td>{tags(line)}</td>
            </tr>
        '''
        print(bib)
        rows.append(bib)
        i += 1

with open(file2, 'w', encoding='utf8') as f:
    heading = '''
    <table class="tablesorter">
    <thead>
        <tr>
            <th>Title</th>
            <th>Authors</th>
            <th>Venue</th>
            <th>Year</th>
            <th>Link(s)</th>
            <th>Arxiv</th>
            <th>Tags</th>
        </tr>
    </thead>
    <tbody>
    '''
    f.write(template.replace('{}', heading+''.join(rows)+'\n</tbody>\n</table>'))