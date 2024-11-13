rule all:
    input:
        "wordCount.txt"

rule create_input:
    output:
        "exampleText.txt"
    shell:
        "echo 'As I walk through the valley of the shadow of death' > {output}"

rule count:
    input:
        "exampleText.txt"
    output:
        "wordCount.txt"
    shell:
        "cat {input} | python3 wordCount.py > {output}"


