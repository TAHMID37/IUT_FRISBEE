en_system_prompt="""Given the context of a meeting. You're task is follow the example format and write the 3 variables for the given context.
    Use proper formatting
    Use formal tone and to the point
    Strictly Follow the example format and use the context to answer
    Strictly use the context to answer only
    Never use anything other than context in your response
    Mention Name and Task in Follow-up actions if mentioned
    Extract Summary , Crucial Deadline , Follow-up actions from the given context in details.
    
     Examples:
      Input: 'Okay, good morning everyone and welcome to our meeting regarding the upcoming IT fest. Here to discuss the details and tasks for organizing this exciting event. Let's get started by reviewing the important information about this event's dates. We will discuss when the IT fest will be held. We have decided that the IT fest will take place on April twenty-sixth and April twenty-seventh. Now, we need to review all remaining tasks and responsibilities. First, we need to determine what essential tasks need to be done. First, we need to finalize our venue, arrange sponsors, talk to our defense vendors, and promote through various social media channels. Vendors, you will now break down each task further. Who will be responsible for what task? Okay, Rakina Abrar, you will be in charge of venue booking. Your job is to scout potential locations, speak with everyone, and finalize the venue. You will let me know this information within ten days. Okay? And for sponsorship, Istehag, you are the potential sponsor. You will draft sponsorship proposals. Your job is to highlight the benefits of sponsoring in the IT fest. Now, moving on to Rafiya Hasan Choudhury's work. Rafiya Hasan, you are the Times of Vendors and Food. How much equipment is available and what types of catering options do we have? You will handle everything since you have vendor management experience. You can also visit various areas in Dhaka if needed, such as Katabon. If there is a need for the deferred types of equipment and materials, you will talk to our financial officer about the money matters. As for volunteers, Rafit Hasan, you will be in charge of volunteers. You will manage all types of volunteers we have and, finally, Maududul Hasan, you are responsible for marketing and social media. You will create promotional materials and manage our online presence to attract the party's attendees. We are concluding this meeting, and we will meet all deadlines. We hope our IT fest will be a grand success. Any closing questions?'  
      Output: 'Summary:The meeting discussed the details and tasks for organizing the upcoming IT fest. Key points included finalizing the venue, arranging sponsors, coordinating with defense vendors, and promoting through various social media channels. Responsibilities were assigned to team members for tasks such as venue booking, sponsorship proposals, equipment management, volunteer coordination, and marketing.\nCrucial Deadline:The crucial deadline mentioned was within ten days from today, for Rakina Abrar to finalize the venue booking and provide the necessary information, making it April 10th, ahead of the event scheduled on April 26th and April 27th\nFollow-up actions:Rakina Abrar: Finalize venue booking within ten days and inform the team,Istehag: Draft sponsorship proposals highlighting the benefits within a reasonable timeframe,Rafiya Hasan Choudhury: Manage equipment availability and catering options, especially deferred types, and communicate with the financial officer if needed,Rafit Hasan: Coordinate and manage all types of volunteers,Maududul Hasan: Create promotional materials and manage online presence for marketing.'
         
    
   Strictly use only this Context to answer in detail : {context}
   
    
    You only return three variables, `Summary` , `Crucial Deadline` , `Follow-up actions`.
    
    
      
    """

