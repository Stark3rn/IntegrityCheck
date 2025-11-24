rule ExampleRule
{
    meta:
        description = "Test rule to detect the word 'malware'"
        author = "IntegrityCheck Test"

    strings:
        $malware_string = "malware"

    condition:
        $malware_string
}
