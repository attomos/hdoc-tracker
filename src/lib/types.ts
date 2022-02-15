export type Tweet = {
  text: string;
  entities: Entities;
  created_at: string;
  public_metrics: PublicMetrics;
  conversation_id: string;
  id: string;
};

export type TweetResponse = {
  data: Tweet[];
};

export type Entities = {
  hashtags?: Hashtag[] | null;
  urls?: TweetUrl[] | null;
  days?: HdocDay[] | null;
};

export type Hashtag = {
  start: number;
  end: number;
  tag: string;
};

export type TweetUrl = {
  start: number;
  end: number;
  url: string;
  expanded_url: string;
  display_url: string;
};

export type HdocDay = {
  start: number;
  end: number;
  day: string;
};

export type PublicMetrics = {
  retweet_count: number;
  reply_count: number;
  like_count: number;
  quote_count: number;
};
