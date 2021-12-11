import ezgmail

def attachment_download(result_threads):
    count_of_results = len(result_threads)
    try:
        for i in range(count_of_results):
            if len(result_threads[i].messages) > 1:
                for j in range(len(result_threads[i].messages)):
                    result_threads[i].messages[j].downloadAllAttachments()
            else:
                result_threads[i].messages[0].downloadAllAttachments()
        print("Downloaded into the root folder Successfully!")
    except:
        raise Exception("Error: Couldn't download attachments!")


if __name__ == '__main__':
    query = input("Enter search query: ")
    newquery = query + " + has:attchment"
    resultthreads = ezgmail.search(newquery)

    if len(resultthreads) == 0:
        print("Result has no attachments:")
    else:
        print("Results with attachments: ")
        for threads in resultthreads:
            print(f"Email Subject: {threads.messages[0].subject}")
        try:
            ask = input("Do you want to download the attachment(s) in the result(s) - (Yes/No) ?")
            if ask =="Yes":
                attachment_download(resultthreads)
            else:
                print("Program Terminated!")
        except:
            print("Something went wrong!")
