import enquiries

options = ['Cat','Dog','Horse']

answer = enquiries.choose('Select favorite animals', options)
print(answer)

answer = enquiries.choose('Select favorite animals', options, multi=True)
print(answer)